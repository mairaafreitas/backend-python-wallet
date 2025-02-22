from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from app.services.calculate_cashback import calculate_cashback
from app.models import Cashback
from app.services.send_cashback import customer_cashback
from app.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = CashbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        total_data = data['total']

        cashback_calculation = calculate_cashback(total_data)

        document = data['customer']['document']

        customer_cashback(document, cashback_calculation)

        serializer.create(data)

        return Response({f"cashback_calculation: {cashback_calculation}"})


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


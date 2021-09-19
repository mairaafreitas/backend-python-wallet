from decimal import Decimal

from rest_framework import viewsets, views
from rest_framework.response import Response

from app.models import Cashback
from app.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = CashbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        total_data = data['total']
        print(total_data)

        cashback_calculation = total_data * Decimal('0.10')
        print(cashback_calculation)

        serializer.create(data)

        return Response({f"cashback_calculation: {cashback_calculation}"})



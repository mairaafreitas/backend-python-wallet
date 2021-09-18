from rest_framework import viewsets
from app.models import Cashback
from app.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer
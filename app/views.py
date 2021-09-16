from django.shortcuts import render
from rest_framework import viewsets
from app.models import Cashback, Customer, Product
from app.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer

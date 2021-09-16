from rest_framework import serializers
from app.models import Cashback, Product, Customer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['type', 'value', 'qty']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['document', 'name']


class CashbackSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    customer = CustomerSerializer()

    class Meta:
        model = Cashback
        fields = ['sold_at', 'customer', 'total', 'products']

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

    def create(self, validated_data):
        customer_validated_data = validated_data.pop('customer')
        customer, created_customer = Customer.objects.get_or_create(
            document=customer_validated_data['document'],
            name=customer_validated_data['name'],
        )

        cashback = Cashback.objects.create(
            sold_at=validated_data['sold_at'],
            total=validated_data['total'],
            customer=customer
        )

        products_validated_data = validated_data.pop('products')
        for product in products_validated_data:
            cashback.products.create(
                type=product['type'],
                value=product['value'],
                qty=product['qty']
            )

        return cashback
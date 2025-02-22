from rest_framework import serializers
from app.models import Cashback, Product, Customer
from validate_docbr import CPF

from app.services.calculate_total import calculate_total


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['type', 'value', 'qty']

    def validate_type(self, type):
        valid_types = ["A", "B", "C"]
        if type not in valid_types:
            raise serializers.ValidationError('Invalid Product Type. Valid types are: "A", "B" or '
                                              '"C"')
        return type


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['document', 'name']

    def validate_document(self, document):
        cpf = CPF()
        if not cpf.validate(document):
            raise serializers.ValidationError('Invalid Document')

        return document


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

    def validate(self, attrs):
        attrs = super(CashbackSerializer, self).validate(attrs)  # calling default validation
        products = attrs['products']
        total_products = calculate_total(products)

        if total_products != attrs['total']:
            raise serializers.ValidationError("The price sum isn't right, check it.")
        return attrs

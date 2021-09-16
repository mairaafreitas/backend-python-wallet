from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class Customer(models.Model):
    document = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    name = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return self.type


class Cashback(models.Model):
    sold_at = models.DateTimeField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    products = models.ManyToManyField('Product')

    def __str__(self):
        return f"Cashback #{self.id}"
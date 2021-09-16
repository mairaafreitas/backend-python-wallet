from django.db import models


class Customer(models.Model):
    document = models.PositiveBigIntegerField()
    name = models.CharField(max_length=80, blank=False)


class Products(models.Model):
    type = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.PositiveIntegerField()


class Cashback(models.Model):
    sold_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    products = models.ManyToManyField(Products)

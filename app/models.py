from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


class Customer(models.Model):
    """Database model for product in the system"""
    document = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    name = models.CharField(max_length=80, blank=False)

    def __str__(self):
        """Return string representation of customer"""
        return self.name


class Product(models.Model):
    """Database model for customer in the system"""
    type = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.PositiveIntegerField()

    def __str__(self):
        """Return string representation of product"""
        return self.type


class Cashback(models.Model):
    """Database model for cashback in the system"""
    sold_at = models.DateTimeField()
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=2, validators=[MinValueValidator(0)])
    products = models.ManyToManyField('Product')

    def __str__(self):
        """Return string representation of cashback and id"""
        return f"Cashback #{self.id}"
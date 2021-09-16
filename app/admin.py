from django.contrib import admin
from app.models import Cashback, Customer, Products


class ManageCashback(admin.ModelAdmin):
    list_display = ('id', 'sold_at', 'customer', 'total')


admin.site.register(Cashback, ManageCashback)
admin.site.register(Customer)
admin.site.register(Products)

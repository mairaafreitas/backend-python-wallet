from django.contrib import admin
from django.urls import path, include
from app.views import CashbackViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cashback', CashbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

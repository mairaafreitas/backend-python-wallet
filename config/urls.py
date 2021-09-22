from django.contrib import admin
from django.urls import path, include

from app.views import CashbackViewSet, UserLoginApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cashback', CashbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

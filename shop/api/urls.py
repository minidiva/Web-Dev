from django.urls import re_path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

from . import views

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)  # /api/categories/
router.register(r"products", ProductViewSet)      # /api/products/


urlpatterns = [
    path("", include(router.urls)),
]

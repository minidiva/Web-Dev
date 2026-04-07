from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from .views.fbv import products_list, product_detail
from .views.cbv import ProductListAPIView as CbvProductList, ProductDetailAPIView as CbvProductDetail
from .views.mixins import ProductListAPIView as MixinProductList, ProductDetailAPIView as MixinProductDetail
from .views.generics import ProductListAPIView as GenericProductList, ProductDetailAPIView as GenericProductDetail

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("fbv/products/", products_list),
    path("fbv/products/<int:product_id>/", product_detail),
    path("cbv/products/", CbvProductList.as_view()),
    path("cbv/products/<int:product_id>/", CbvProductDetail.as_view()),
    path("mixins/products/", MixinProductList.as_view()),
    path("mixins/products/<int:product_id>/", MixinProductDetail.as_view()),
    path("generics/products/", GenericProductList.as_view()),
    path("generics/products/<int:product_id>/", GenericProductDetail.as_view()),
]
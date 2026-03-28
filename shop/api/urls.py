from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^products/$", views.get_products),
    re_path(r"^products/(?P<id>\d+)/$", views.get_product_by_id),
    re_path(r"^categories/$", views.get_categories),
    re_path(r"^categories/(?P<id>\d+)/$", views.get_category_by_id),
    re_path(r"^categories/(?P<id>\d+)/products/$", views.get_category_products),
]

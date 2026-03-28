from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# /api/categories/

# /api/categories/<int:id>/

# /api/categories/<int:id>/products/

def get_products(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)

def get_product_by_id(request, id):
    product = Product.objects.filter(id=id).values().first()
    return JsonResponse(product, safe=False)

def get_categories(request):
    categories = Category.objects.all().values()
    return JsonResponse(list(categories), safe=False)

def get_category_by_id(request, id):
    category = Category.objects.filter(id=id).values().first()
    return JsonResponse(category, safe=False)

def get_category_products(request, id):
    products = Product.objects.filter(category_id=id).values()
    return JsonResponse(list(products), safe=False)


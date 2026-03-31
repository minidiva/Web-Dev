from django.http import JsonResponse
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action


# /api/categories/<id>/products/
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(detail=True, methods=["get"], url_path="products")
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

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


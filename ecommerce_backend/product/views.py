from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from ecommerce_backend.product.serializers import ProductSerializer, CategorySerializer, BrandSerializer
from ecommerce_backend.product.models import Product, Category, Brand

class CategoryViewSet(viewsets.ViewSet):
    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()

    @action(methods=['get'], detail=False,url_path = r"category/(?P<category>\w+)/all")
    def list_product_by_category(self, request, category):
        serialized = ProductSerializer(Product.objects.filter(category__name=category))
        return Response(serialized.data)
    
    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

class BrandViewSet(viewsets.ViewSet):
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from apps.products.models import (
    ProductAuto, Product, Category,
    CategoryAuto
)

from apps.products.serializers import(
    ProductAutoSerializer,
    ProductSerializer, 
    CategorySerializer,
    CategoryAutoSerializer
)


class ProductView(ReadOnlyModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )

    search_fields = (
        'name', 'category__name',
    )
    filterset_fields = (
        'in_stock', 'category'
    )


class ProductAutoView(ReadOnlyModelViewSet):
    queryset = ProductAuto.objects.filter()
    serializer_class = ProductAutoSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, )

    filterset_fields = (
        'in_stock', 'category'
    )
    search_fields = (
        'name', 'category__name',
    )


class CategoryView(ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

class CategoryAutoView(ReadOnlyModelViewSet):
    queryset = CategoryAuto.objects.filter(is_active=True)
    serializer_class = CategoryAutoSerializer

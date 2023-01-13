from rest_framework import serializers

from apps.products.models import (
    Product, ProductAuto,
    ProductImage, ProductAutoImage,
    Category, CategoryAuto
)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image', )


class ProductAutoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAutoImage
        fields = ('image', )


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


class ProductAutoSerializer(serializers.ModelSerializer):
    images = ProductAutoImageSerializer(many=True, read_only=True)
    class Meta:
        model = ProductAuto
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAuto
        fields = '__all__'

from django.contrib import admin

from apps.products.models import (
    ProductAuto, ProductAutoImage,
    Product, ProductImage,
    Category,CategoryAuto
)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


class ProductAutoImageInline(admin.TabularInline):
    model = ProductAutoImage
    extra = 3


class ProductAutoAdmin(admin.ModelAdmin):
    inlines = [
        ProductAutoImageInline,
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAuto, ProductAutoAdmin)
admin.site.register(Category)
admin.site.register(CategoryAuto)

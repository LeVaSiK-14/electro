from rest_framework.routers import DefaultRouter as DR

from apps.products.views import (
    ProductView, ProductAutoView,
    CategoryView, CategoryAutoView
)

router = DR()

router.register('products', ProductView, basename='product')
router.register('product_auto', ProductAutoView, basename='product_auto')
router.register('category', CategoryView, basename='category')
router.register('category', CategoryView, basename='category')
router.register('category_auto', CategoryAutoView, basename='category_auto')


urlpatterns = [

]

urlpatterns += router.urls

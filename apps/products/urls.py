from rest_framework.routers import DefaultRouter as DR

from apps.products.views import (
    ProductView, ProductAutoView,
    CategoryView, 
)

router = DR()

router.register('products', ProductView, basename='product')
router.register('product_auto', ProductAutoView, basename='product_auto')
router.register('category', CategoryView, basename='category')

urlpatterns = [

]

urlpatterns += router.urls

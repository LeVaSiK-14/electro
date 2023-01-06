from rest_framework.routers import DefaultRouter as DR

from apps.company_info.views import (
    CompanyInfoView,
)


router = DR()

router.register('company_info', CompanyInfoView, basename='company_info')

urlpatterns = [
]

urlpatterns += router.urls

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from apps.company_info.models import CompanyInfo
from apps.company_info.serializers import CompanyInfoSerializer


class CompanyInfoView(ReadOnlyModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

    def list(self, request, *args, **kwargs):
        return Response(CompanyInfoSerializer(CompanyInfo.objects.first()).data)

from rest_framework import serializers

from apps.company_info.models import(
    CompanyInfo, Slider,
)


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('image', )


class CompanyInfoSerializer(serializers.ModelSerializer):
    images = SliderSerializer(read_only=True, many=True)

    class Meta:
        model = CompanyInfo
        fields = '__all__'

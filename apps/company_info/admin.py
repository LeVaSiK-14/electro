from django.contrib import admin
from django.conf import settings

from apps.company_info.models import CompanyInfo, Slider


class SliderInline(admin.TabularInline):
    model = Slider
    extra = 3


class CompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= settings.MAX_CONTACTS_COUNT:
            return False
        return super().has_add_permission(request)
    
    inlines = [
        SliderInline,
    ]


admin.site.register(CompanyInfo, CompanyAdmin)

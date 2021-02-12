from django.contrib import admin
from .models import Certificate
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CertificateResource(resources.ModelResource):
    class Meta:
        model = Certificate

class CertificateAdmin(ImportExportModelAdmin):
    resource_class = CertificateResource


admin.site.register(Certificate, CertificateAdmin)

from django.contrib import admin
from .models import Certificate
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CertificateResource(resources.ModelResource):
    class Meta:
        model = Certificate

class CertificateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CertificateResource
    list_display = ('name','email','event', 'image_created', 'email_sent')

admin.site.register(Certificate, CertificateAdmin)

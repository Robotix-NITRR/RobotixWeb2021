from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Contact
# Register your models here.
# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass

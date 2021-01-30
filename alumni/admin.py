from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Alumni
# Register your models here.
# admin.site.register(Alumni)
@admin.register(Alumni)
class AlumniAdmin(ImportExportModelAdmin):
    pass

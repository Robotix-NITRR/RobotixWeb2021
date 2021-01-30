from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Gallery
# Register your models here.

# admin.site.register(Gallery)
@admin.register(Gallery)
class GalleryAdmin(ImportExportModelAdmin):
    pass

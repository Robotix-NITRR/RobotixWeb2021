from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import FYI,DIY,sponsors, web ,app
# Register your models here.
# admin.site.register(FYI)
# admin.site.register(DIY)
admin.site.register(web)
admin.site.register(app)

@admin.register(FYI)
class FYIAdmin(ImportExportModelAdmin):
    pass

@admin.register(DIY)
class DIYAdmin(ImportExportModelAdmin):
    pass

@admin.register(sponsors)
class sponsorsAdmin(ImportExportModelAdmin):
    pass

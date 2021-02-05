from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ca,Timer,recruitment
# Register your models here.
admin.site.register(Timer)


# @admin.register(ca)
# admin.site.register(Recruitment)
# class WorkshopsView(ImportExportModelAdmin):
#     pass


@admin.register(recruitment)
# admin.site.register(Recruitment)
class recruitmentView(ImportExportModelAdmin):
    pass

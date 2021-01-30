from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Achievements
# Register your models here.
# admin.site.register(Achievements)
@admin.register(Achievements)
class AchievementsAdmin(ImportExportModelAdmin):
    pass

from django.contrib import admin
from .models import portalUser,Team,problem_statement
from import_export.admin import ImportExportModelAdmin


@admin.register(portalUser)
class portalUserAdmin(ImportExportModelAdmin):
    pass

@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    pass

@admin.register(problem_statement)
class problem_statementAdmin(ImportExportModelAdmin):
    pass


# Register your models here.
# admin.site.register(portalUser)
# admin.site.register(problem_statement)
# admin.site.register(Token)
# admin.site.register(Team)

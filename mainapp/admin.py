from django.contrib import admin
from .models import Diagnostic, Organisation
from import_export.admin import ImportExportMixin


class DiagnosticAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['created', 'gr', 'ga', 'gia', 'gav', 'cea', 'iic',
                    'ri', 'gde', 'cp', 'gpc', 'total', 'id_organization']


class OrganisationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['org_name']


admin.site.register(Diagnostic, DiagnosticAdmin)
admin.site.register(Organisation, OrganisationAdmin)

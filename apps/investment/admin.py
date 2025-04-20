from django.contrib import admin
from .models import Fund, FundUpdate

@admin.register(Fund)
class FundAdmin(admin.ModelAdmin):
    list_display = ('name', 'structure', 'institution', 'launch', 'currency')
    list_filter = ('structure', 'institution', 'currency')

@admin.register(FundUpdate)
class FundUpdateAdmin(admin.ModelAdmin):
    list_display = ('name', 'fund_value', 'return_last_30_days', 'number_of_contributors', 'updated_at')
    sortable_by = ('name', 'fund_value', 'return_last_30_days', 'number_of_contributors', 'updated_at')
    ordering = ['-fund_value']
    
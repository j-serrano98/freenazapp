from django.contrib import admin
from .models import PaymentMethod, TransactionCategory, Transaction


admin.site.register(PaymentMethod)


@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type', 'name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'tax', 'currency', 'name', 'type', 'category', 'status', 'ref')
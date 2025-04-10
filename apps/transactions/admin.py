from django.contrib import admin
from .models import PaymentMethod, TransactionCategory, Transaction


admin.site.register(PaymentMethod)
admin.site.register(TransactionCategory)
admin.site.register(Transaction)
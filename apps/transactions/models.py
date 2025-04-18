from django.db import models
from django.conf import settings


class PaymentMethod(models.Model):
     name = models.CharField(max_length=100)
     user = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name="payment_methods"
         )
     
     def __str__(self):
          return self.name
     
class TransactionCategory(models.Model):
    class TypeChoices(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"
        INVESTMENT = "INVESTMENT", "Investment"

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TypeChoices, default=TypeChoices.EXPENSE)
    user = models.ForeignKey(
         settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name="categories",
         null=True, blank=True
         )
     
    def __str__(self):
        return f"{self.name}"
    
class Transaction(models.Model):

    class CurrencyChoices(models.TextChoices):
         DOP = "DOP", "DOP"
         USD = "USD", "USD"
         EUR = "EUR", "EUR"    

    class StatusChoices(models.TextChoices):
        SUCCESSFUL = "SUCCESSFUL", "Successful"  
        CANCELLED = "CANCELLED", "Cancelled"  

    type = models.CharField(max_length=10, choices=TransactionCategory.TypeChoices, default=TransactionCategory.TypeChoices.EXPENSE)
    currency = models.CharField(max_length=3, choices=CurrencyChoices, default=CurrencyChoices.DOP)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, default="")
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(TransactionCategory, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=StatusChoices)
    ref = models.CharField(max_length=9, null=True, blank=True)
    related_transaction = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='tax_transactions')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
     


    def __str__(self):
        return f"{self.name} - {self.amount} {self.currency}"
     

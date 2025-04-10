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

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=7, choices=TypeChoices.choices)
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

    type = models.CharField(max_length=7, choices=TransactionCategory.TypeChoices, default=TransactionCategory.TypeChoices.INCOME)
    currency = models.CharField(max_length=3, choices=CurrencyChoices, default=CurrencyChoices.DOP)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    name = models.CharField(max_length=255)
    method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(TransactionCategory, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=StatusChoices)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
     


    def __str__(self):
        return f"{self.name} - {self.amount} {self.currency}"
     

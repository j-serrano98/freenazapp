from django.urls import path
from .views import TransactionCreateView

app_name = 'transactions'

urlpatterns = [
    path('', TransactionCreateView.as_view(), name='transactions'),
]

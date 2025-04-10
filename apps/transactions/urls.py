from django.urls import path
from .views import TransactionsPageView

app_name = 'transactions'

urlpatterns = [
    path('', TransactionsPageView.as_view(), name='transactions'),
]

from django.urls import path
from .views import TransactionCreateView, CategoryCreateView

app_name = 'transactions'

urlpatterns = [
    path('', TransactionCreateView.as_view(), name='transactions'),
    path('categories/', CategoryCreateView.as_view(), name='categories'),
]

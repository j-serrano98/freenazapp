from django.urls import path
from .views import HomePageView, TransactionsPageView

app_name = 'core'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('transactions/', TransactionsPageView.as_view(), name='transactions'),
]

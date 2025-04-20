from django.urls import path
from .views import InvestmentCreateView

app_name = 'investment'

urlpatterns = [
    path('', InvestmentCreateView.as_view(), name='investment'),
    # path('compare/', CompareView.as_view(), name='compare'),
]

from django.views.generic import TemplateView
from .models import 

# Create your views here.
class TransactionsPageView(TemplateView):
    template_name = 'transactions/transactions.html'
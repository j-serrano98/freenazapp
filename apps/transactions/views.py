from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .models import Transaction
from .forms import TransactionForm
from django.http import HttpResponseRedirect


class TransactionCreateView(LoginRequiredMixin, FormMixin, ListView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transactions.html'
    context_object_name = 'transactions'
    success_url = reverse_lazy('transactions:transactions')
    login_url = "users:login"

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        transaction.formatted_date = transaction.date.strftime("%m%d%y")
        transaction.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
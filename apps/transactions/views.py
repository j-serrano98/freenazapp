from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .models import Transaction, TransactionCategory
from .forms import TransactionForm, TransactionCategoryForm
from django.http import HttpResponseRedirect
from .utils import create_transaction_ref


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
        refs = create_transaction_ref()
        transaction.ref = refs[0]
        # transaction.formatted_date = transaction.date.strftime("%m%d%y")
        transaction.save()

        if transaction.tax > 0:
            Transaction.objects.create(
                user = self.request.user,
                type = transaction.type,
                currency = transaction.currency,
                amount = transaction.tax,
                name = transaction.name,
                description = f"Tax for transaction {transaction.ref}",
                method = transaction.method,
                category = transaction.category,
                status = transaction.status,
                ref = refs[1],
                related_transaction=transaction
                )
            
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    

class CategoryCreateView(LoginRequiredMixin, FormMixin, ListView):
    model = TransactionCategory
    form_class =  TransactionCategoryForm
    template_name = 'transactions/categories.html'
    success_url = reverse_lazy('transactions:categories')
    login_url = 'users:login'

    def get_queryset(self):
        return TransactionCategory.objects.filter(user=self.request.user).order_by('name')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        user = self.request.user


        context['income_categories'] = TransactionCategory.objects.filter(user=user).filter(type=TransactionCategory.TypeChoices.INCOME)
        context['expense_categories'] = TransactionCategory.objects.filter(user=user).filter(type=TransactionCategory.TypeChoices.EXPENSE)
        context['investment_categories'] = TransactionCategory.objects.filter(user=user).filter(type=TransactionCategory.TypeChoices.INVESTMENT)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form):
        category = form.save(commit=False)
        category.user = self.request.user
        category.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
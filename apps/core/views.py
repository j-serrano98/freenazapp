from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.transactions.models import Transaction
from django.db.models import Sum
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/overview.html'
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        user = self.request.user
        now = datetime.now()

        # TOTAL INCOMES
        total_incomes = Transaction.objects.filter(user=user).filter(type="INCOME").aggregate(Sum("amount"))["amount__sum"] or 0
        formatted_total =  f"{total_incomes:,.2f}"
        integer_part, decimal_part = formatted_total.split(".")
        context['total_incomes_integer'] = integer_part
        context['total_incomes_decimal'] = decimal_part


        # TOTAL EXPENSES
        total_expenses = Transaction.objects.filter(user=user).filter(type="EXPENSE").aggregate(Sum("amount"))["amount__sum"] or 0
        formatted_total =  f"{total_expenses:,.2f}"
        integer_part, decimal_part = formatted_total.split(".")
        context['total_expenses_integer'] = integer_part
        context['total_expenses_decimal'] = decimal_part

        # TOTAL BALANCE
        total_balance = f"{total_incomes - total_expenses:,.2f}"
        integer_part, decimal_part = total_balance.split(".")
        context['total_balance_integer'] = integer_part
        context['total_balance_decimal'] = decimal_part
        # context['total_balance'] = f"{total_incomes - total_expenses:,.2f}"

        # LAST TRANSACTIONS
        context['recent_transactions'] = Transaction.objects.filter(user=user).order_by('-date')[:3]

        # TOTAL TRANSACTIONS
        monthly_qs = Transaction.objects.filter(
            user=user,
            date__year=now.year,
            date__month=now.month
        ).order_by('-date')

        monthly_data = list(monthly_qs.values('amount', 'category'))
        context['monthly_transactions'] = json.dumps(monthly_data, cls=DjangoJSONEncoder)



        return context
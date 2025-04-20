from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
# from django.views.generic.edit import FormMixin
# from django.urls import reverse_lazy
# from django.http import HttpResponseRedirect
from .models import FundUpdate
from django.db.models import OuterRef, Subquery


class InvestmentCreateView(LoginRequiredMixin, ListView):
    model = FundUpdate
    template_name = 'investment/compare_investment.html'
    context_object_name = 'investments'

    def get_queryset(self):
        last_updated = FundUpdate.objects.filter(name=OuterRef('name')).order_by('-updated_at')
        return_last_updated = FundUpdate.objects.filter(pk=Subquery(last_updated.values('pk')[:1])).order_by('name')
        return return_last_updated
    

class CompareView(TemplateView):
    pass
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.transactions.models import Transaction

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/overview.html'
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        user = self.request.user

        context['recent_transactions'] = Transaction.objects.filter(user=user).order_by('-date')[:3]

        return context
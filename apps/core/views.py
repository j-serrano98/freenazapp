from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'core/overview.html'
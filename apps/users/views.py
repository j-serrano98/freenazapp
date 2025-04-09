from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth.views import LoginView


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('core:home')


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('core:home')

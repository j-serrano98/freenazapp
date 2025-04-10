from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    # success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        new_user = form.save()
        authenticate_user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )

        if authenticate_user is not None:
            login(self.request, authenticate_user)
        return redirect('core:home')
    


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('core:home')

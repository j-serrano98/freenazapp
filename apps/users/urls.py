from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    RegisterView,
    CustomLoginView
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]




"""
Profile update

Password reset/change

"""
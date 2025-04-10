from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("", include('apps.core.urls')),
    path('users/', include('apps.users.urls')),
    path('transactions/', include('apps.transactions.urls')),
]

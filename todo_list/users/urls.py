from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import dashboard, register

app_name = 'dashboard'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dash/', dashboard, name='index'),
    path('register/', register, name='register'),
]
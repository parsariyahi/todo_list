from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), #auth routes
    path('dash/', views.dashboard, name='index'),
    path('register/', views.register, name='register'),
]
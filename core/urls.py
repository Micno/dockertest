# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('setup-guide/', views.SetupGuideView.as_view(), name='setup_guide'),
]


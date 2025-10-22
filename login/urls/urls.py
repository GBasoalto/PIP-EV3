from django.contrib import admin
from django.urls import path
from login.views.views import LoginFormView, HomePageView

urlpatterns = [
    path('',LoginFormView.as_view(), name='login'),
    path('inicio/', HomePageView.as_view(), name='home'),
    
]

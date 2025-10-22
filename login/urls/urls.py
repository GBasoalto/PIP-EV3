from django.contrib import admin
from django.urls import path
from login.views.views import LoginFormView, HomePageView, RecuperarPasswordView,LogoutView

urlpatterns = [
    path('',LoginFormView.as_view(), name='login'),
    path('inicio/', HomePageView.as_view(), name='home'),
    path('recuperar/', RecuperarPasswordView.as_view(), name='recuperar'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]

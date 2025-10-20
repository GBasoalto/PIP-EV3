from django.contrib import admin
from django.urls import path
from login.views.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginView.as_view(), name='login'),
    
]

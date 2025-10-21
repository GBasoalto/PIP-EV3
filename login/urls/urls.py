from django.contrib import admin
from django.urls import path
from login.views.views import LoginFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',LoginFormView.as_view(), name='login'),
    
]

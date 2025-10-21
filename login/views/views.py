from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from login.forms import LoginForm

# class LoginView(TemplateView):
#     template_name = "login.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Login"

#         return context

class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/inicio/'  


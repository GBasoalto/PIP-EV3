from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from login.forms import LoginForm
from login.models import usuario
from django.contrib import messages


#NECESITO CAMBIAR EL METODO PARA SI NO SE ENCUENTRA LOGUEADO IR A LOGIN 
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        user_id = self.request.session.get('user_id')
        if not user_id:
            return redirect(reverse('login'))
        
        context['user'] = usuario.objects.get(id=user_id)
        context['title'] = "Inicio"
        return context

    def get(self, request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')  # Aquí sí se puede redirigir
        return super().get(request, *args, **kwargs)
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

    cargos = ['Médico','Matrón','enfermero','Administrativo']

    def form_valid(self, form):
        correo = form.cleaned_data['correo']
        password = form.cleaned_data['password']

        try:
            user = usuario.objects.get(correo=correo)
        except usuario.DoesNotExist:
            messages.error(self.request, "Correo o contraseña incorrectos")
            return self.form_invalid(form)

        if not user.activo:
            messages.error(self.request, "Su cuenta ha sido bloqueada, comuníquese con área de TI")
            return self.form_invalid(form)

        #MANEJO DE INTENTOS 
        if user.password != password:
            user.intentos += 1
            if user.intentos >= 3:
                user.activo = False
            user.save()
            messages.error(self.request, f"Contraseña incorrecta ({user.intentos}/3)")
            return self.form_invalid(form)
        else:
            user.intentos = 0 
            user.save()

        #SI NO SE ENCUENTRA EN LOS CARGOS CREADOS
        if user.tipo_cargo.cargo not in self.cargos:
            messages.error(self.request, "No tiene permisos para ingresar")
            return self.form_invalid(form)

        self.request.session['user_id'] = user.id  #GUARDAR EL USUARIO ID
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
        


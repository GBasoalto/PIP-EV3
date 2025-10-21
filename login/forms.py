from django import forms
from .models import usuario


#CREAR FORMULARIO PARA EL INICIO DE SESION (REEMPLAZAR DE FORMA DINAMICA EN LA CARD DE BOOSTRAP)
class LoginForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['correo', 'password'] 
        widgets = {
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }
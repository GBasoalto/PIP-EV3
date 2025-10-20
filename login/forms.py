from django import forms
from .models import usuario


#CREAR FORMULARIO PARA EL INICIO DE SESION (REEMPLAZAR DE FORMA DINAMICA EN LA CARD DE BOOSTRAP)
class LoginForm(forms.ModelForm):
    class Meta: 
        model = usuario
        fields = ['usuario', 'password']
        widgets = {
            'usuario' : forms.TextInput(),
            'password' :forms.PasswordInput(),
        }
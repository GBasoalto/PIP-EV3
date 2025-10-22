from django import forms


#CREAR FORMULARIO PARA EL INICIO DE SESION (REEMPLAZAR DE FORMA DINAMICA EN LA CARD DE BOOSTRAP)
class LoginForm(forms.Form):
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
   
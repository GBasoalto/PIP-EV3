from django.db import models

# Create your models here.

class cargo(models.Model):
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.cargo

#solo médicos, matrones, enfermeros y administrativo del hospital pueden ingresar , podria haber un usuario y denegar la entrada
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True) 
    password = models.CharField(max_length=100)
    tipo_cargo = models.ForeignKey(cargo, on_delete=models.CASCADE) #BUSCAR COMO INDEXAR CON EL ID DEL CARGO
    intentos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre



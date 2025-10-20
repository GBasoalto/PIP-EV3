from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField
    password = models.CharField(max_length=100)
    tipo_cargo = models.IntegerField #BUSCAR COMO INDEXAR CON EL ID DEL CARGO

    def __str__(self):
        return self.name

#solo médicos, matrones, enfermeros y administrativo del hospital pueden ingresar , podria haber un usuario y denegar la entrada

class cargo(models.Model):
    cargo = models.CharField(max_length=100)
from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    hash_senha = models.CharField(max_length=512)

    def __str__(self):
        return self.email
    
class Curso(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    duration = models.BigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fotos = models.ImageField(upload_to='cursos/fotos/', null=True, blank=True)

class Login(models.Model):
    usuario = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=16)

class foto(models.Model):
    nome = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='imagens/')
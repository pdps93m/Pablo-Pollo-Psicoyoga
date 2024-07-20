from django.db import models
from django.contrib.auth.models import User 

from django.utils.timezone import datetime  


# Modelo de negocio de la Aplicación.

class Estilo(models.Model):
    nombre = models.CharField(max_length=50, default="Sin estilo")
    estilo = models.CharField(max_length=50, default="Sin estilo")
    horarios = models.CharField(max_length=50, default="Sin estilo")
    
    """class Meta:
        orderimg = ["nombre"]"""
        
    def __str__(self):
        return f"{self.nombre}"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    
    """class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["nombre", "apellido"]"""""
        
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
        
"""class Consultas(models.Model):
    nombre = models.CharField(max_length=60)
    pregunta = models.CharField(max_length=500,default="Sin estilo")
    email = models.EmailField()"""
    
class Ac_terapeutico(models.Model):
    nombre = models.CharField(max_length=60,default="Sin estilo")
    asist_semanales = models.CharField(max_length=50,default="Sin estilo")
    horario = models.CharField(max_length=50,default="Sin estilo")
    email = models.EmailField()
    

    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user} {self.imagen}"
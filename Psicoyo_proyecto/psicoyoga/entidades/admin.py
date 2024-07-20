from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Estilo)
admin.site.register(Alumno)
#admin.site.register(Consultas)
admin.site.register(Ac_terapeutico)
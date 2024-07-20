from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 


class EstiloForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre del Alumno")
    estilo = forms.CharField(max_length=50, required=True, label="Nombre del Estilo")
    horarios = forms.CharField(max_length=50, required=True)
    
class AlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre del Alumno")
    apellido = forms.CharField(required=True)
    email = forms.CharField(max_length=50, required=True)
    
class Ac_terapForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre del Paciente")
    asist_semanales = forms.CharField(max_length=50,required=True)
    horario = forms.CharField(max_length=50, required=True, label="Horario de Concurrencia")
    email = forms.EmailField(max_length=50,required=True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class ReservarForm(forms.Form):
    paciente_nombre = forms.CharField(max_length=50, required=True, label="Nombre del Paciente")
    paciente_asist_semanales = forms.CharField(max_length=50,required=True)
    paciente_horario = forms.CharField(max_length=50, required=True, label="Horario de Concurrencia")
    paciente_email = forms.EmailField(max_length=50,required=True)
    
class UsuarioEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="nombre", max_length=50, required=True)
    last_name = forms.CharField(label="apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

    
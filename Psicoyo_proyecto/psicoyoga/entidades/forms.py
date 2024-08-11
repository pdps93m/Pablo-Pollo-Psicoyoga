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
    
    
class RegistroForm(UserCreationForm):
    User = forms.CharField(max_length=50, required=True, label="Nombre de usuario")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
    
class UsuarioEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="nombre", max_length=50, required=True)
    last_name = forms.CharField(label="apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    
class ConsultaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, label="Nombre")
    email = forms.EmailField(required=True)
    consulta_motivo = forms.CharField(max_length=255, required=True)
    consulta_mensaje = forms.CharField(widget=forms.Textarea, required=True)
    
    class Meta:
        model = User
        fields = ["nombre", "email", "motivo", "mensaje"]

class ConsultaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    
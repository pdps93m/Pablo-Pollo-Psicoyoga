from django.shortcuts import render, redirect
from .models import *
from entidades.static import*
from .forms import *
from django.template import loader

from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

 
# Create your views here.

def home(request):
    return render(request, "entidades/index.html")

#def consultas(request):
    contexto = {"consultas": Consultas.objects.all()}
    return render(request, "entidades/consultas.html", contexto)

def datos_mios(request):
    return render(request, "entidades/datos_mios.html")

@login_required
def ac_terapeutico(request):
    contexto = {"acompañamiento_terapeutico": Ac_terapeutico.objects.all()}
    return render(request, "entidades/ac_terapeutico.html", contexto )

#_____ Estilo
#def estilo(request):
    contexto = {"estilo": Estilo.objects.all()}
    return render(request, "entidades/estilo.html", contexto)

#def estiloForm(request):
    if request.method == "POST":
       miForm =EstiloForm(request.POST)
       if miForm.is_valid():
           nombre = miForm.cleaned_data.get("nombre")
           estilo = miForm.cleaned_data.get("estilo")
           horarios = miForm.cleaned_data.get("horarios")
           estilo = Estilo(nombre=nombre, estilo=estilo, horarios=horarios)
           estilo.save()
           contexto = {"estilo": Estilo.objects.all()}
           return render(request, "entidades/estilo.html", contexto)
    else:
        miForm = EstiloForm()
    
    return render(request, "entidades/estiloForm.html", {"form": miForm})

#def estiloUpdate(request, id_estilo):
    estilo = Estilo.objects.get(id=id_estilo) 
    if request.method == "POST":
       miForm =EstiloForm(request.POST)
       if miForm.is_valid():
           estilo.nombre = miForm.cleaned_data.get("nombre")
           estilo.estilo = miForm.cleaned_data.get("estilo")
           estilo.horarios = miForm.cleaned_data.get("horarios")
           estilo.save()
           contexto = {"estilo": Estilo.objects.all()}
           return render(request, "entidades/estilo.html", contexto) 
    else:
        miForm = EstiloForm(initial={"nombre": estilo.nombre, "estilo": estilo.estilo, "horarios": estilo.horarios})   

    return render(request, "entidades/estiloForm.html", {"form": miForm})

#def estiloDelete(request, id_estilo):
    estilo = Estilo.objects.get(id=id_estilo) 
    estilo.delete()
    contexto = {"estilo": Estilo.objects.all()}
    return render(request, "entidades/estilo.html", contexto) 
    
    
#______ Alumno
#def alumno(request):
    contexto = {"alumno": Alumno.objects.all()}
    return render(request, "entidades/alumno.html", contexto)

#def alumnoForm(request):
    if request.method == "POST":
        miForm =AlumnoForm(request.POST)
        if miForm.is_valid():
           nombre = miForm.cleaned_data.get("nombre")
           apellido = miForm.cleaned_data.get("apellido")
           email = miForm.cleaned_data.get("email")
           alumno = Alumno(nombre=nombre, apellido=apellido, email=email)
           alumno.save()
           contexto = {"alumno": Alumno.objects.all()}
           return render(request, "entidades/alumno.html", contexto) 
    else:
        miForm = AlumnoForm()
    
    return render(request, "entidades/alumnoForm.html", {"form": miForm})

#def alumnoUpdate(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno) 
    if request.method == "POST":
       miForm =AlumnoForm(request.POST)
       if miForm.is_valid():
           alumno.nombre = miForm.cleaned_data.get("nombre")
           alumno.apellido = miForm.cleaned_data.get("apellido")
           alumno.email = miForm.cleaned_data.get("email")
           alumno.save()
           contexto = {"alumno": Alumno.objects.all()}
           return render(request, "entidades/alumno.html", contexto) 
    else:
        miForm = AlumnoForm(initial={"nombre": alumno.nombre, "apellido": alumno.apellido, "email": alumno.email})   

    return render(request, "entidades/alumnoForm.html", {"form": miForm})


#def alumnoDelete(request, id_alumno):
    alumno = Alumno.objects.get(id=id_alumno) 
    alumno.delete()
    contexto = {"alumno": Alumno.objects.all()}
    return render(request, "entidades/alumno.html", contexto) 

@login_required
def ac_terapForm(request):
    if request.method == "POST":
        miForm = Ac_terapForm(request.POST)
        if miForm.is_valid():
           paciente_nombre = miForm.cleaned_data.get("nombre")
           asist_semanales = miForm.cleaned_data.get("asist_semanales")
           paciente_horario = miForm.cleaned_data.get("horario")
           paciente_email = miForm.cleaned_data.get("email") 
           ac_terapeutico = Ac_terapeutico(nombre=paciente_nombre, asist_semanales=asist_semanales, horario=paciente_horario, email=paciente_email)
           ac_terapeutico.save()
           contexto = {"ac_terapeutico": Ac_terapeutico.objects.all()}
           return render(request, "entidades/ac_terapeutico.html", contexto)
    else:
        miForm = Ac_terapForm()
    
    return render(request, "entidades/ac_terapForm.html", {"form": miForm})


#______Buscar
@login_required
def buscarEstilo(request):
    return render(request,"entidades/buscar.html")

@login_required
def encontrarEstilo(request):
    if request.GET["buscar"]:   
        patron = request.GET["buscar"]
        estilo = Estilo.objects.filter(nombre__icontains=patron)
        contexto = {'estilo': estilo}
    else:
        contexto = {'estilo': Estilo.objects.all()}
        
    return render(request, "entidades/estilo.html", contexto)


@login_required
def buscarAlumno(request):
    return render(request,"entidades/buscar.html")

@login_required
def encontrarAlumno(request):
    if request.GET["buscar"]:   
        patron = request.GET["buscar"]
        alumno = Alumno.objects.filter(nombre__icontains=patron)
        contexto = {'alumno': alumno}
    else:
        contexto = {'alumno': Alumno.objects.all()}
        
    return render(request, "entidades/alumno.html", contexto)



 #_____ Resolución de alumno con Class Base View 
 
class AlumnoList(LoginRequiredMixin, ListView):     # Esto simplifica la primer linea del def alumno
    model = Alumno
    
class AlumnoCreate(LoginRequiredMixin, CreateView):
    model = Alumno
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("alumno")
    
class AlumnoUpdate(LoginRequiredMixin, UpdateView):
    model = Alumno
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("alumno")
    
class AlumnoDelete(LoginRequiredMixin, DeleteView):
    model = Alumno
    success_url = reverse_lazy("alumno")
    

#_____ Resolución de estilo con Class Base View 
 
class EstiloList(LoginRequiredMixin, ListView):     # Esto simplifica la primer linea del def estilo
    model = Estilo
    
class EstiloCreate(LoginRequiredMixin, CreateView):
    model = Estilo
    fields = ["nombre", "estilo", "horario"]
    success_url = reverse_lazy("estilo")
    
class EstiloUpdate(LoginRequiredMixin, UpdateView):
    model = Estilo
    fields = ["nombre", "estilo", "horario"]
    success_url = reverse_lazy("estilo")
    
class EstiloDelete(LoginRequiredMixin, DeleteView):
    model = Estilo
    success_url = reverse_lazy("estilo")
    
    
# ______ Login, Logout, Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            #_________ Buscar Avatar
            try:
                avatar = Avatar.objets.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
        
    else:
        miForm = AuthenticationForm()
        
    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    
    else:
        miForm = RegistroForm()
        
    return render(request, "entidades/registro.html", {"form": miForm})

#@login_required
#def reservar_hora(request):
    if request.method == "POST":
        miForm = ReservarForm(request.POST)
        if miForm.is_valid():
            paciente_nombre = miForm.cleaned_data.get("nombre")
            paciente_asist_semanales = miForm.cleaned_data.get("asistencias")
            paciente_horario = miForm.cleaned_data.get("horario")
            paciente_email = miForm.cleaned_data.get("email")
            miForm.save()
            return redirect(reverse_lazy('reservar_sesion.html', {"form": miForm}))
    
    
# ________ Editar Perfil / Avatar

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UsuarioEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UsuarioEditForm(instance=usuario)
    return render(request, "entidades/perfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambio_clave.html"
    success_url = reverse_lazy("home")
    
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambio_clave.html"
    success_url = reverse_lazy("home")
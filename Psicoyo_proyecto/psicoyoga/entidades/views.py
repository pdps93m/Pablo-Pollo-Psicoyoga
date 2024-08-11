from django.shortcuts import render, redirect
from .models import *
from entidades.static import*
from .forms import *
from django.template import loader

from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .forms import ConsultaForm
 
# Create your views here.

def home(request):
    return render(request, "entidades/index.html")


def datos_mios(request):
    return render(request, "entidades/datos_mios.html")


def ac_terapeutico(request):
    return render(request, "entidades/ac_terapeutico.html")

def estilo(request):
    return render(request, "entidades/estilo.html")



#______Buscar

def buscar(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        resultados_estilos = Estilo.objects.filter(nombre__icontains=busqueda)
        resultados_alumnos = Alumno.objects.filter(nombre__icontains=busqueda)
        return render(request, 'entidades/resultados.html', {
            'resultados_estilos': resultados_estilos,
            'resultados_alumnos': resultados_alumnos,
        })
    else:
        return render(request, 'entidades/busqueda.html', )

def resultados_estilos(request):
    
    estilo_id = request.GET.get('estilo_id')
    estilo = Estilo.objects.get(id=estilo_id)

    
    alumnos_estilo = estilo.alumno_set.all()

    context = {
        'estilo': estilo,
        'alumnos_estilo': alumnos_estilo,
    }
    return render(request, 'resultados/estilos.html', context)

def resultados_alumnos(request):
    
    alumno_id = request.GET.get('alumno_id')
    alumno = Alumno.objects.get(id=alumno_id)

   
    estilos_alumno = alumno.estilo_set.all()

    context = {
        'alumno': alumno,
        'estilos_alumno': estilos_alumno,
    }
    return render(request, 'resultados/alumnos.html', context)


@login_required
def buscarEstilo(request):
    if request.GET['buscar']:  # Si hay un término de búsqueda
        patron = request.GET["buscar"]
        estilo = Estilo.objects.filter(nombre__icontains=patron)
        contexto = {'estilo': estilo}
    else:
        return render(request, 'entidades/buscarEstilo.html')
    

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
    return render(request,"entidades/buscarAlumno.html")

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
    fields = ["nombre", "estilo", "horarios"]
    success_url = reverse_lazy("estilo")
    
class EstiloUpdate(LoginRequiredMixin, UpdateView):
    model = Estilo
    fields = ["nombre", "estilo", "horarios"]
    success_url = reverse_lazy("estilo")
    
class EstiloDelete(LoginRequiredMixin, DeleteView):
    model = Estilo
    success_url = reverse_lazy("estilo")
    
#_____ Resolución de Ac Terapeutico con Class Base View 
class ac_terap_List(ListView):    
    model = Ac_terapeutico
    
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
            User.first_name = miForm.cleaned_data.get("username")  
            miForm.save()
            return redirect(reverse_lazy('home'))
    
    else:
        miForm = RegistroForm()
        
    return render(request, "entidades/registro.html", {"form": miForm})


    
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

@login_required    
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #__________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #_________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            #__________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambio_clave.html"
    success_url = reverse_lazy("home")





def realizarConsulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email'] 
            consulta_motivo = form.cleaned_data['motivo']
            consulta_mensaje = form.cleaned_data['mesnsaje']

            send_mail(
                consulta_motivo,
                consulta_mensaje,
                email,
                ['pdps93m@gmail.com'], 
            )
            mensaje_confirmacion = f"¡Gracias {nombre}! Hemos recibido tu consulta y te responderemos a la brevedad a {email}." 
            context = {'mensaje_confirmacion': mensaje_confirmacion}
            return render(request, 'entidades/confirmacionConsulta.html.', context)

        else:
            context = {'form': form}
            return render(request, 'entidades/confirmacionConsulta.html', context)
    else:
        form = ConsultaForm() 
        context = {'form': form}
        return render(request, 'index.html', context)




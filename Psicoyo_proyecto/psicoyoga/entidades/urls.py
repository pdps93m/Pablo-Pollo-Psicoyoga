from django.urls import path, include
from .views import *
from entidades import views
from entidades.views import AlumnoDelete
from entidades.views import *

from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', home, name="home"),
    
    
    path('datos_mios/', views.datos_mios, name="datos_mios"),
    #path('consultas/', views.consultas, name="consultas"),
    
    
    
    #_____ Estilos
    path('estilo/', EstiloList.as_view(), name="estilo"),
    path('estiloCreate/', EstiloCreate.as_view(), name="estiloCreate"),
    path('estiloUpdate/<int:pk>/', EstiloUpdate.as_view(), name="estiloUpdate"),   
    path('estiloDelete/<int:pk>/', EstiloDelete.as_view(), name="estiloDelete"),   

    
    #path('estiloForm/', estiloForm, name="estiloForm"),
    #path('estiloUpdate/<id_estilo>/', estiloUpdate, name="estiloUpdate"),
    #path('estiloDelete/<id_estilo>/', estiloDelete, name="estiloDelete"),

    #_____ Alumno
    path('alumno/',AlumnoList.as_view(), name="alumno"),
    #path('alumnoForm/', alumnoForm, name="alumnoForm"),
    path('alumnoCreate/',AlumnoCreate.as_view(), name="alumnoCreate"),
    path('alumnoUpdate/<int:pk>/', AlumnoUpdate.as_view(), name="alumnoUpdate"),   
    path('alumnoDelete/<int:pk>/', AlumnoDelete.as_view(), name="alumnoDelete"),   

    #_____ Ac Terapeutico
    path('ac_terapeutico/', views.ac_terapeutico, name="ac_terapeutico"),
    #path('ac_terapForm/', ac_terapForm, name="ac_terapForm"),
     
    #_____Busquedas
    path('buscarEstilo/', buscarEstilo, name="buscarEstilo"),
    path('encontrarEstilo/', encontrarEstilo, name="encontrarEstilo"),
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
    path('encontrarAlumno/', encontrarAlumno, name="encontrarAlumno"),
    
    
    
    #______ Alumno CCBV
    
    #path('alumno/',AlumnoList.as_view(), name="alumno"),
    
    
    #______ Alumno create
    path('alumnoCreate/',AlumnoList.as_view(), name="alumnoCreate"),
    
    #______ Alumno delete
    path('alumnoDelete/<int:pk>/', AlumnoDelete.as_view(), name="alumnoDelete"),   

    
    #______ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    
    #______ Edición de Perfil / Avatar
    path('perfil/', editarPerfil, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar clave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),


    


    

        

]



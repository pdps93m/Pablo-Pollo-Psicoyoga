from django.urls import path, include
from .views import *
from entidades import views
from entidades.views import AlumnoDelete
from entidades.views import *

from django.contrib.auth.views import LogoutView, LoginView



 


urlpatterns = [
    path('', home, name="home"),
    
    
    path('datos_mios/', views.datos_mios, name="datos_mios"),
    
    
    path('realizarConsulta/', views.realizarConsulta, name="realizarConsulta"),
    path('confirmacionConsulta/', views.realizarConsulta, name='enviar_consulta'),
    
    
    
    
        #_____ Estilos
    path('estilo/', EstiloList.as_view(), name="estilo"),
    path('estiloCreate/', EstiloCreate.as_view(), name="estiloCreate"),
    path('estiloUpdate/<int:pk>/', EstiloUpdate.as_view(), name="estiloUpdate"),   
    path('estiloDelete/<int:pk>/', EstiloDelete.as_view(), name="estiloDelete"),   


    #_____ Alumno
    path('alumno/',AlumnoList.as_view(), name="alumno"),
    path('alumnoCreate/',AlumnoCreate.as_view(), name="alumnoCreate"),
    path('alumnoUpdate/<int:pk>/', AlumnoUpdate.as_view(), name="alumnoUpdate"),   
    path('alumnoDelete/<int:pk>/', AlumnoDelete.as_view(), name="alumnoDelete"),   


    #_____ Ac Terapeutico
    path('ac_terapeutico/', views.ac_terapeutico, name="ac_terapeutico"),
    
     
    #_____Busquedas
    path('buscarEstilo/', buscarEstilo, name="buscarEstilo"),
    path('encontrarEstilo/', views.encontrarEstilo, name="estiloForm"),
    path('buscarAlumno/', buscarAlumno, name="buscarAlumno"),
    path('encontrarAlumno/', views.encontrarAlumno, name="alumnoForm"),
    
    path('busqueda/', views.buscar, name="busqueda"),
    path('resutados/', views.resultados_alumnos, name="resultados"),
    path('resutados/', views.resultados_estilos, name="resultados"),
    path('resultados/estilos/<int:estilo_id>/', views.resultados_estilos, name='resultados_estilos'),
    path('resultados/alumnos/<int:alumno_id>/', views.resultados_alumnos, name='resultados_alumnos'),
    
    
    #______ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    
    #______ Edición de Perfil / Avatar
    path('perfil/', editarPerfil, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar clave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),


    


    

        

]



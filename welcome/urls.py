#url patterns for the welcome app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # Ruta para la página principal
    path('login/', views.user_login, name='login'),  # Ruta para iniciar sesión
    path('logout/', views.user_logout, name='logout'),  # Ruta para cerrar sesión
    path('register/', views.register, name='register'),  # Ruta para registrar usuarios
    path('error_escritura/', views.error_escritura, name='error_escritura'),  # Ruta para el error de escritura
    path('error_sistema/', views.error_sistema, name='error_sistema'),  # Ruta para el error de sistema
]
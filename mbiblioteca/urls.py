
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios_list/', views.usuarios_list, name='usuarios_list'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('edit_usuario/<int:id>/', views.edit_usuario, name='edit_usuario'),
    path('del_usuario/<int:id>/', views.del_usuario, name='del_usuario'),
    path('libros_list/', views.libros_list, name='libros_list'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_libro/<int:autor_id>', views.crear_libro, name='crear_libro'),
    path('edit_libro/<int:id>/', views.edit_libro, name='edit_libro'),
    path('del_libro/<int:id>/', views.del_libro, name='del_libro'),
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('login_view/', views.login_view, name='login_view'),
    path('index_login/', views.index_login, name='index_login'),
]

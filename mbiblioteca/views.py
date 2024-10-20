from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from . import models as datos
from .models import Usuario, Autor, Libro
from .forms import UsuarioForm, UsuarioEditForm, AutorForm, LibroForm, LibroEditForm, LoginForm
from django.utils import timezone
from django.db.models import Q


# Create your views here.


def index(request):
    return render(request, 'mbiblioteca/index.html')


def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'mbiblioteca/usuarios_list.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuarioForm()
    return render(request, 'mbiblioteca/crear_usuario.html', {'form': form})


def edit_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if request.method == 'POST':
        form = UsuarioEditForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.fecha_modificacion = timezone.now()
            form.save()
            return redirect('usuarios_list')
    else:
        form = UsuarioEditForm(instance=usuario)

    return render(request, 'mbiblioteca/edit_usuario.html', {'form': form, 'usuario': usuario})


def del_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')

    return render(request, 'usuarios_list', {'usuario': usuario})


def libros_list(request):
    libros = Libro.objects.all()
    return render(request, 'mbiblioteca/libros_list.html', {'libros': libros})


def crear_autor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)

        if autor_form.is_valid():
            autor = autor_form.save()

            return redirect('crear_libro')
    else:
        autor_form = AutorForm()

    return render(request, 'mbiblioteca/crear_autor.html', {
        'autor_form': autor_form
    })


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('libros_list')
    else:
        form = LibroForm()

    return render(request, 'mbiblioteca/crear_libro.html', {
        'form': form
    })


def edit_libro(request, id):
    libro = get_object_or_404(Libro, id=id)

    if request.method == 'POST':
        form = LibroEditForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros_list')
    else:
        form = LibroEditForm(instance=libro)

    return render(request, 'mbiblioteca/edit_libro.html', {'form': form})


def del_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros_list')

    return render(request, 'mbiblioteca/libros_list.html', {'libro': libro})


def buscar_libro(request):
    query = request.GET.get('q')
    if query:
        libros = Libro.objects.filter(
            Q(titulo__icontains=query))
    else:
        libros = Libro.objects.none()

    return render(request, 'mbiblioteca/buscar_libro.html', {'libros': libros})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        nombre = request.POST.get('nombre')
        contrasena = request.POST.get('contrasena')

        try:
            usuario = Usuario.objects.get(nombre=nombre)
            if usuario.contrasena == contrasena:
                return redirect('index_login')
            else:
                return render(request, 'mbiblioteca/login_view.html', {'error_message': 'Contraseña incorrecta', 'form': form})
        except Usuario.DoesNotExist:
            return render(request, 'mbiblioteca/login_view.html', {'error_message': 'El usuario no existe', 'form': form})
    else:
        form = LoginForm()
    return render(request, 'mbiblioteca/login_view.html', {'form': form})


def index_login(request):
    return render(request, 'mbiblioteca/index_login.html')

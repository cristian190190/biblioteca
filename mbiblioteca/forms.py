from django import forms
from .models import Usuario, Autor, Libro
from .choices import idioma, rol, estado


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'contrasena', 'id_rol', 'estado']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'contrasena': 'Contraseña',
            'id_rol': 'Rol',
            'estado': 'Estado'
        }
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre', 'required': 'required', 'id': 'nombre'}),
            
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo', 'required': 'required', 'id': 'correo', 'type' : 'email'}),
            
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña', 'required': 'required', 'id': 'contrasena'}),
            
            'id_rol': forms.Select(choices=rol, attrs={'class': 'form-control', 'placeholder': 'Seleccione un rol', 'required': 'required', 'id': 'id_rol'}),
            
            'estado': forms.Select(choices=estado, attrs={'class': 'form-control', 'placeholder': 'Seleccione un estado', 'required': 'required', 'id': 'estado'})
        }

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['fecha_creacion', 'contraseña']
        fields = ['nombre', 'correo', 'id_rol', 'estado']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'id_rol': 'Rol',
            'estado': 'Estado'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre', 'required': 'required', 'id': 'nombre'}),
            
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su correo', 'required': 'required', 'id': 'correo'}),
            
            'id_rol': forms.Select(choices=rol, attrs={'class': 'form-control', 'placeholder': 'Seleccione un rol', 'required': 'required', 'id': 'id_rol'}),
            
            'estado': forms.Select(choices=estado, attrs={'class': 'form-control', 'placeholder': 'Seleccione un estado', 'required': 'required', 'id': 'estado'})
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'biografia',
                  'fnacimiento', 'nacionalidad', 'estado']
        labels = {
            'nombre': 'Nombre',
            'biografia': 'Biografía',
            'fnacimiento': 'Fecha de Nacimiento',
            'nacionalidad': 'Nacionalidad',
            'estado': 'Estado'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del autor', 'required': 'required', 'id': 'nombre'}),
            
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la biografía del autor', 'required': 'required', 'id': 'biografia'}),
            
            'fnacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha de nacimiento del autor', 'required': 'required', 'id': 'fnacimiento', 'type' : 'date'}),
            
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la nacionalidad del autor', 'required': 'required', 'id': 'nacionalidad'}),
            
            'estado': forms.Select(choices=estado, attrs={'class': 'form-control', 'placeholder': 'Seleccione un estado', 'required': 'required', 'id': 'estado'})
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fpublicacion', 'id_editorial', 'stock', 'nro_paginas', 'idioma', 'estado']
        labels = {
            'titulo': 'Título',
            'fpublicacion': 'Fecha de Publicación',
            'id_editorial': 'ID de Editorial',
            'stock': 'Stock',
            'nro_paginas': 'Número de Páginas',
            'idioma': 'Idioma',
            'estado': 'Estado'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del libro', 'required': 'required', 'id': 'titulo'}),
            
            'fpublicacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha de publicación del libro', 'required': 'required', 'id': 'fpublicacion', 'type': 'date'}),
            
            'id_editorial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la editorial del libro', 'required': 'required', 'id': 'id_editorial'}),
            
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el stock del libro', 'required': 'required', 'id': 'stock'}),
            
            'nro_paginas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de páginas del libro', 'required': 'required', 'id': 'nro_paginas'}),
            
            'idioma': forms.Select(choices=idioma, attrs={'class': 'form-control', 'placeholder': 'Seleccione un idioma', 'required': 'required', 'id': 'idioma'}),
            
            'estado': forms.Select(choices=estado, attrs={'class': 'form-control', 'placeholder': 'Seleccione un estado', 'required': 'required', 'id': 'estado'})
            
        }


class LibroEditForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fpublicacion', 'id_editorial',
                  'stock', 'nro_paginas', 'idioma', 'estado']
        labels = {
            'titulo': 'Título',
            'fpublicacion': 'Fecha de Publicación',
            'id_editorial': 'Editorial',
            'stock': 'Stock',
            'nro_paginas': 'Número de Páginas',
            'idioma': 'Idioma',
            'estado': 'Estado',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del libro', 'required': 'required', 'id': 'titulo'}),

            'fpublicacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la fecha de publicación del libro', 'required': 'required', 'id': 'fpublicacion', 'type': 'date'}),

            'id_editorial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la editorial del libro', 'required': 'required', 'id': 'id_editorial'}),

            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el stock del libro', 'required': 'required', 'id': 'stock'}),

            'nro_paginas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el número de páginas del libro', 'required': 'required', 'id': 'nro_paginas'}),

            'idioma': forms.Select(choices=idioma, attrs={'class': 'form-control', 'placeholder': 'Seleccione un idioma', 'required': 'required', 'id': 'idioma'}),
            
            'estado': forms.Select(choices=estado, attrs={'class': 'form-control', 'placeholder': 'Seleccione un estado', 'required': 'required', 'id': 'estado'})
        }
from django.db import models
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(default=timezone.now)
    id_rol = models.PositiveIntegerField(verbose_name='Rol')
    estado = models.PositiveIntegerField(verbose_name='Estado')
    

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}".format(self.nombre, self.correo, self.contrasena, self.fecha_creacion, self.fecha_modificacion, self.id_rol, self.estado)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre', 'correo', 'contrasena', 'fecha_creacion', 'fecha_modificacion', 'id_rol', 'estado']

class Autor(models.Model):
    
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    biografia = models.TextField(verbose_name='Biografía')
    fnacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    nacionalidad = models.CharField(max_length=50, verbose_name='Nacionalidad')
    estado = models.PositiveIntegerField(verbose_name='Estado')
    
    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.nombre, self.biografia, self.fnacimiento, self.nacionalidad, self.estado)
    
    class Meta:
        db_table = 'autores'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre', 'biografia', 'fnacimiento', 'nacionalidad', 'estado']
        
class Libro(models.Model):
    titulo = models.CharField(max_length=50, verbose_name='Título')
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fpublicacion = models.DateField(verbose_name='Fecha de Publicación')
    id_editorial = models.PositiveIntegerField(verbose_name='Editorial')
    stock = models.PositiveIntegerField(verbose_name='Stock')
    nro_paginas = models.PositiveIntegerField(verbose_name='Número de Páginas')
    idioma = models.PositiveIntegerField(verbose_name='Idioma')
    estado = models.PositiveIntegerField(verbose_name='Estado')
    
    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format(self.titulo, self.id_autor, self.fpublicacion, self.id_editorial, self.stock, self.nro_paginas, self.idioma, self.estado)
    
    class Meta:
        db_table = 'libros'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'id_autor', 'fpublicacion', 'id_editorial', 'stock', 'nro_paginas', 'idioma', 'estado']
    
                              
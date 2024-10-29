from django.db import models

# Create your models here.
class Game(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6) # CharField is used for short texts
    nombre = models.CharField(max_length=50) # CharField requiere max_lenght
    descripcion = models.TextField() # TextField is used for long texts
    precio = models.DecimalField(max_digits=10, decimal_places=2) # DecimalField is used for exact quantities
    plataforma = models.CharField(max_length=50)
    imagenes = models.ImageField(upload_to='juegos_imagenes/', blank=True, null=True) # ImageField is used for save images
    
    def __str__(self):
        return f'{self.nombre} ({self.precio})'

# class Review(models.Model):
    
    
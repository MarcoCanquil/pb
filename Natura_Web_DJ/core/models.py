from django.db import models
from django.core.exceptions import ValidationError

class Producto(models.Model):
    # Opciones para la categoría
    CATEGORIAS_CHOICES = [
        ('perfumería', 'Perfumería'),
        ('maquillaje', 'Maquillaje'),
        ('rostro', 'Rostro'),
        ('cuidados_diarios', 'Cuidados Diarios'),
        ('cabello', 'Cabello'),
        ('infantil', 'Infantil'),
        ('repuestos', 'Repuestos'),
    ]

    # Opciones para la marca
    MARCA_CHOICES = [
        ('ekos', 'Ekos'),
        ('tododia', 'Tododia'),
        ('mama_y_bebe', 'Mamá y Bebé'),
        ('creer_para_ver', 'Creer para Ver'),
        ('erva_doce', 'Erva Doce'),
        ('chronos', 'Chronos'),
        ('kaiak', 'Kaiak'),
        ('lumina', 'Lumina'),
        ('homem', 'Homem'),
        ('ilia', 'Ilía'),
        ('essencial', 'Essencial'),
        ('humor', 'Humor'),
    ]

    nombre = models.CharField(max_length=200)  # Nombre del producto
    marca = models.CharField(max_length=50, choices=MARCA_CHOICES) 
    categoria = models.CharField(max_length=50, choices=CATEGORIAS_CHOICES)  # Categoría del producto
    descripcion = models.TextField()  # Descripción del producto
    precio = models.IntegerField() # Precio del producto
    cantidad = models.PositiveIntegerField(default=0)  # Cantidad disponible en inventario
    imagen = models.ImageField(upload_to='cards/', null=True, blank=True)  # Imagen del producto

    def clean(self):
        # Validar que se haya seleccionado una opción válida
        if not self.marca:
            raise ValidationError('Debe seleccionar una marca válida.')
        if not self.categoria:
            raise ValidationError('Debe seleccionar una categoría válida.')

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} disponibles)"

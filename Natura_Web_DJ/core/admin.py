from django.contrib import admin
from .models import Producto

# Configuración del modelo en el admin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria','marca','precio')  
    search_fields = ('nombre', 'categoria','marca') 
    list_filter = ('categoria','marca')  
    ordering = ('nombre',)  

# Registrar el modelo y su configuración en el admin
admin.site.register(Producto, ProductoAdmin)
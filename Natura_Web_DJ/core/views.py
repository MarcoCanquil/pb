from django.shortcuts import render
from .models import Producto

# Create your views here.

def catalogo(request):

    productos = Producto.objects.all().order_by('-id')   # Obtiene todos los productos

    contexto = {
        'titulo': 'Catálogo',
        'productos': productos,
    }

    return render(request, 'catalogo.html', contexto)


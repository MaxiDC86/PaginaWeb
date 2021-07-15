from django.shortcuts import render
from tienda.models import CategoriaProd, Producto

# Create your views here.

def tienda(request):

    categoria = CategoriaProd.objects.all()
    productos = Producto.objects.all()

    return render(request,"tienda/tienda.html", {"categoria":categoria, "productos":productos} )
from django.shortcuts import render
from django.core.mail import send_mail
from .carro import Carro

from tienda.models import Producto

from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("Tienda")

def eliminar_producto(request, producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Tienda")

def restar_producto(request, producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Tienda")

def limpiar_carro(request):

    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("Tienda")

def comprar(self, request):

    asunto = "Cotizacion"

    mensaje = str(self.session["carro"])

    email = "pepe@gmail.com"

    send_mail(asunto, mensaje, email ,['mdiascorreia86@gmail.com'],fail_silently=False)

    return redirect("Tienda")
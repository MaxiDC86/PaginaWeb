from django.shortcuts import render
from tienda.models import CategoriaProd, Producto


# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK("TEST-1682191286570055-072420-081eaf21dbcddd9e349e4e05abdcad98-97637851")

# Create your views here.

def tienda(request):

    categoria = CategoriaProd.objects.all()
    productos = Producto.objects.all()

    return render(request,"tienda/tienda.html", {"categoria":categoria, "productos":productos} )

def comprar(request):

    categoria = CategoriaProd.objects.all()
    productos = Producto.objects.all()

    return render(request,"tienda/comprar.html", {"categoria":categoria, "productos":productos} )

# Crea un ítem en la preferencia
preference_data = {
    "items": [
        {
            "title": "Mi producto",
            "quantity": 1,
            "unit_price": 75.76,
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
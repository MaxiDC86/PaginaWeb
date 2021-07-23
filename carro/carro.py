from django.core.mail import send_mail

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        
        self.carro = carro

    def agregar(self, producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] ={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"] = value["cantidad"] +1
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto.id =str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"] = value["cantidad"] -1
                if value["cantidad"] <1:
                    self.eliminar(producto)
                break        
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

    def comprar(self,request):

        if self.request.user.is_authenticated:

            asunto = "PEDIDO DE COMPRA CON CARRITO"

            mensaje = ""
            for key, value in self.carro.items():
                mensaje = mensaje + value["nombre"]
                mensaje = mensaje +" cantidad: "+ str(value["cantidad"])
                mensaje = mensaje +" $"+ str(value["precio"]) + "\n"
            mensaje = mensaje + str(self.request.user.username) + "\n" 
            mensaje = mensaje + str(self.request.user.last_name) + "\n" 
            mensaje = mensaje + str(self.request.user.email)
            email = "maxisambo@gmail.com"

            send_mail(asunto, mensaje, email ,['mdiascorreia86@gmail.com'],fail_silently=False)

            # self.session["carro"] = {}
            # self.session.modified = True
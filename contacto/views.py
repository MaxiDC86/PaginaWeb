from django.shortcuts import render
from django.core.mail import send_mail
from contacto.forms import FormularioContacto

# Create your views here.
def contacto(request):

    if request.method =="POST":

        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infForm = miFormulario.cleaned_data

            print(infForm)

            infForm['asunto'] = infForm['nombre'] + ' ' + infForm['asunto']

            infForm['mensaje'] = infForm['mensaje'] + '  ' + infForm['email']

            send_mail(infForm['asunto'], infForm['mensaje'], infForm['email'] ,['mdiascorreia86@gmail.com'],fail_silently=False,)

            return render(request,"contacto/gracias.html")

    else:

        miFormulario=FormularioContacto()

    return render(request,"contacto/formulario_contacto.html", {"form":miFormulario})
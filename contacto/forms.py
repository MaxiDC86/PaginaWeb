from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=300)
    asunto = forms.CharField(max_length=300)
    email = forms.EmailField()
    mensaje = forms.CharField(max_length=3000)
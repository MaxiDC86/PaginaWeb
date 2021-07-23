from django.test import TestCase

from django.urls import path

from . import views


urlpatterns = [
   
 path('',views.tienda, name="Tienda"),
 path('comprar/',views.comprar, name="Comprar"),

]

from django.contrib import admin
from .models import CategoriaProd, Producto
# Register your models here.


class CategoriaProdAdmin(admin.ModelAdmin):
    pass

class ProductoAdmin(admin.ModelAdmin):
    pass

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
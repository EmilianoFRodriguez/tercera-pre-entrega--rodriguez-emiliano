from django.contrib import admin
from .models import Cliente, Producto, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'dni')
    ordering = ('apellido', 'nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'marca', 'precio')
    search_fields = ('nombre', 'categoria', 'tipo', 'marca')
    ordering = ('nombre', 'marca')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'fecha_pedido', 'fecha_entrega')
    list_filter = ('estado', 'fecha_pedido')
    search_fields = ('cliente__nombre', 'producto__nombre')
    ordering = ('-fecha_entrega',)
    date_hierarchy = 'fecha_pedido'




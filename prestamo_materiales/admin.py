from django.contrib import admin
from .models import Material, Pedido

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
	model = Material

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
	model = Pedido	

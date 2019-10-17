from rest_framework import serializers

from . import SERIALIZATION_MODULES

class MaterialSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'nro_material',
			'nro inventario'
		)
		model = models.Material

class PedidoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'fecha',
			'nombre_alumno',
			'apellido_alumno',
			'material',
			'estado_producto_entregado',
			'estado_producto_devuelto',
			'cantidad_materiales'
		)
		model = models.Pedido

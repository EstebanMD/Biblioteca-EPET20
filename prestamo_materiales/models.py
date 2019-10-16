from django.db import models

class Material(models.Model):
	nombre_material = models.CharField(max_length=50)
	nro_inventario = models.IntegerField()

class Pedido(models.Model):
	fecha = models.DateField()
	nombre_alumno = models.CharField(max_length=50)
	apellido_alumno = models.CharField(max_length=50)
	material = models.ForeignKey(Material, on_delete=models.CASCADE)
	estado_producto_entregado = models.CharField(max_length=50)
	estado_producto_devuelto = models.CharField(max_length=50)
	cantidad_materiales = models.IntegerField()

from django.db import models

ESTADOS_MATERIAL = (
	('No entregado', 'No entregado'),
	('Buenas condiciones', 'Buenas condiciones'),
	('Malas condiciones', 'Malas condiciones'),
)

ESTADOS = (
	('Buenas condiciones', 'Buenas condiciones'),
	('Malas condiciones', 'Malas condiciones'),
)

class Material(models.Model):
	nombre_material = models.CharField(help_text='Ingrese nombre del material solicitado', max_length=50)

	def __str__(self):
		return '%s' % (self.nombre_material)

	class Meta:
		verbose_name = 'Material'
		verbose_name_plural = 'Materiales'
		#ordering = ['nombre_material']

class Pedido(models.Model):
	fecha = models.DateField(auto_now_add=True, help_text='Ingrese la fecha en que se realiza el pedido')
	hora = models.DateTimeField(auto_now=True)
	nombre_alumno = models.CharField(help_text='Ingrese nombre del alumno que realiza el pedido', max_length=50)
	apellido_alumno = models.CharField(help_text='Ingrese el apellido del alumno', max_length=50)
	material = models.CharField(help_text='Ingrese material solicitado', max_length=70)
	cantidad_materiales = models.PositiveSmallIntegerField(help_text='Ingrese la cantidad de productos solicitados')
	estado_producto_entregado = models.CharField(help_text='Ingrese el estado del producto entregado', 
		choices=ESTADOS, default='Buenas condiciones', max_length=50)
	estado_producto_devuelto = models.CharField(help_text='Ingrese el estado del producto una vez este fue devuelto', 
		choices=ESTADOS_MATERIAL, default='No entregado', max_length=50,)
	devuelto = models.BooleanField(default=False)

	def __str__(self):
		return 'Pedido de %s' % (self.apellido_alumno)

	class Meta:
		verbose_name = 'pedido'
		verbose_name_plural = 'pedidos'
		ordering = ['-id']

#from rest_framework import status #nose que es, pero lo importa para crear/listar cursos (stage1)
#from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import generics
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pedido
from . import models
from . import serializers

class ListarCrearPedidoView(generics.ListCreateAPIView): #django rest framework, sacado de los videos
	queryset = models.Pedido.objects.all()
	serializer_class = serializers.PedidoSerializer

class RecuperarActualizarEliminarPedido(generics.RetrieveUpdateDestroyAPIView):#django rest framework, sacado de los videos
	queryset = models.Pedido.objects.all()
	serializer_class = serializers.PedidoSerializer

class IndexView(TemplateView):# Templates, sacado de distintas paginas y de su repositorio
	template_name = 'index.html'

class ListarPedidos(ListView):
	model = Pedido
	template_name = 'listado_pedidos.html'
	context_object_name = 'pedidos'

class PedidosSinEntregar(TemplateView):
	model = Pedido
	template_name = 'no_entregados.html'
	context_object_name = 'pedidos'
	
	
class PedidosCreate(CreateView):#LoginRequiredMixin
	model = Pedido
	fields = ['nombre_alumno', 'apellido_alumno', 'material', 'estado_producto_entregado', 
	'estado_producto_devuelto', 'cantidad_materiales'] #'fecha', 
	template_name = 'pedidos_create.html'
	success_url = reverse_lazy('prestamo_materiales:index')
		
class PedidosUpdate(UpdateView):
	model = Pedido
	fields = ['nombre_alumno', 'apellido_alumno', 'material', 'estado_producto_entregado', 
	'estado_producto_devuelto', 'cantidad_materiales'] #'fecha', 
	template_name = 'pedido_update.html'
	context_object_name = 'pedidos'

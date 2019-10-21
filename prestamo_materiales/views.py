#from rest_framework import status #nose que es, pero lo importa para crear/listar cursos (stage1)
#from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import generics
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

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
	success_url = reverse_lazy ('templates/principal')

class ListarPedidos(TemplateView): #No anda
	template_name = 'principal.html'

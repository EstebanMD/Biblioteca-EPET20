#from rest_framework import status #nose que es, pero lo importa para crear/listar cursos (stage1)
#from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import generics

from . import models
from . import serializers

class ListarCrearPedidoView(generics.ListCreateAPIView):
	queryset = models.Pedido.objects.all()
	serializer_class = serializers.PedidoSerializer

class RecuperarActualizarEliminarPedido(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Pedido.objects.all()
	serializer_class = serializers.PedidoSerializer

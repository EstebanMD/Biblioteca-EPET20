from rest_framework import status #nose que es, pero lo importa para crear/listar cursos
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class ListarCrearPedidoView(APIView):
	def get(self, request, format=None):
		pedidos = models.Pedido.objects.all()
		serializer = serializers.PedidoSerializer(pedidos, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.PedidoSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
		







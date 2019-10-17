#
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class ListarPedidoView(APIView):
	def get(self, request, format=None):
		pedidos = models.Pedido.objects.all()
		serializer = serializers.PedidoSerializer(pedidos, many=True)
		return Response(serializer.data)

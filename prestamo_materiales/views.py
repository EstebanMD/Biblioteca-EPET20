#
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class ListarPedidos(APIView):
	def get(self, request, format=none):
		pedido = models.Pedido.objects.all()
		serializer = serializers.PedidoSerializer(pedido, many=True)
		Return Response(serializer.data)

from django.urls import path
from . import views
from .views import IndexView, ListarPedidos, PedidosSinEntregar, PedidosCreate, PedidosUpdate

app_name = 'prestamo_materiales'
urlpatterns = [
	#path('', views.ListarCrearPedidoView.as_view(), name='ListarPedidos'),
	#path('<pk>/', 
	#	views.RecuperarActualizarEliminarPedido.as_view(),
	#	name='pedido_detalle'),
	path('listar', ListarPedidos.as_view(), name='listado_pedidos'),
	path('', IndexView.as_view(), name='index'),
	path('sin_entregar', PedidosSinEntregar.as_view(), name='no_entregados'),
	path('crear/', PedidosCreate.as_view(), name='pedidos_create'),
	path('actualizar', PedidosUpdate.as_view(), name='pedido_update')
]

from django.urls import path
from . import views
from .views import IndexView

app_name = 'prestamo_materiales'
urlpatterns = [
	path('', views.ListarCrearPedidoView.as_view(), name='ListarPedidos'),
	path('<pk>/', 
		views.RecuperarActualizarEliminarPedido.as_view(),
		name='pedido_detalle'),
	path('sign_in', IndexView.as_view(), name='index'),
	path('', ListarPedidos.as_view(), name='listado_pedidos'),
]

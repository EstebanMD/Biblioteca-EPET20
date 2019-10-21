from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListarCrearPedidoView.as_view(), name='ListarPedidos'),
	path('<pk>/', 
		views.RecuperarActualizarEliminarPedido.as_view(),
		name='pedido_detalle'),
	path('sign_in', views.index, name='index'),
]

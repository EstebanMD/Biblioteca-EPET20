from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListarPedidoView.as_view(), name='ListarPedidos'),

]
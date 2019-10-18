from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListarCrearPedidoView.as_view(), name='ListarPedidos'),

]
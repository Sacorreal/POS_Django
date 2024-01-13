from rest_framework import generics

from .models import Categoria, Cliente, Pedido, Producto
from .serializers import (CategoriaProductoSerializer, CategoriaSerializer,
                          ClienteSerializer, PedidoSerializer,
                          ProductoSerializer)


#Solo método GET
class CategoriaListView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

#metodo GET y POST
class ClienteView(generics.ListCreateAPIView): 
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Cliente.objects.all()
    lookup_url_kwarg = 'cliente_id'
    serializer_class = ClienteSerializer

class CategoriaProductosView(generics.RetrieveAPIView): 
    queryset = Categoria.objects.all()
    lookup_url_kwarg = 'categoria_id'
    serializer_class = CategoriaProductoSerializer

#solo método POST
class PedidoCreateView(generics.CreateAPIView): 
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
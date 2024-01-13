from api.models import Categoria, Producto
from api.serializers import CategoriaSerializer, ProductoSerializer
from rest_framework import viewsets


class CategoriaViewSet(viewsets.ModelViewSet): 
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer



from rest_framework import viewsets
from .models import (
    Ciudades, Clientes, Vendedores, Categorias, Productos,
    Estados, Ventas, Credencialescliente, Credencialesvendedor,
    Metodopago, Metodosenvio, Pedidos, Detallepedido,
    Historialbusqueda, Resenias
)
from .serializers import (
    CiudadesSerializer, ClientesSerializer, VendedoresSerializer,
    CategoriasSerializer, ProductosSerializer, EstadosSerializer,
    VentasSerializer, CredencialesClienteSerializer,
    CredencialesVendedorSerializer, MetodoPagoSerializer,
    MetodosEnvioSerializer, PedidosSerializer,
    DetallePedidoSerializer, HistorialBusquedaSerializer,
    ReseñasSerializer
)

class CiudadesViewSet(viewsets.ModelViewSet):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class VendedoresViewSet(viewsets.ModelViewSet):
    queryset = Vendedores.objects.all()
    serializer_class = VendedoresSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class EstadosViewSet(viewsets.ModelViewSet):
    queryset = Estados.objects.all()
    serializer_class = EstadosSerializer


class VentasViewSet(viewsets.ModelViewSet):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer


class CredencialesClienteViewSet(viewsets.ModelViewSet):
    queryset = Credencialescliente.objects.all()
    serializer_class = CredencialesClienteSerializer


class CredencialesVendedorViewSet(viewsets.ModelViewSet):
    queryset = Credencialesvendedor.objects.all()
    serializer_class = CredencialesVendedorSerializer


class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = Metodopago.objects.all()
    serializer_class = MetodoPagoSerializer


class MetodosEnvioViewSet(viewsets.ModelViewSet):
    queryset = Metodosenvio.objects.all()
    serializer_class = MetodosEnvioSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = Detallepedido.objects.all()
    serializer_class = DetallePedidoSerializer


class HistorialBusquedaViewSet(viewsets.ModelViewSet):
    queryset = Historialbusqueda.objects.all()
    serializer_class = HistorialBusquedaSerializer


class ReseñasViewSet(viewsets.ModelViewSet):
    queryset = Resenias.objects.all()
    serializer_class = ReseñasSerializer

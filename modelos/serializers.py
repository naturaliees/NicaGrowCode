from rest_framework import serializers
from .models import (
    Ciudades,
    Clientes,
    Vendedores,
    Categorias,
    Productos,
    Estados,
    Ventas,
    Credencialescliente,
    Credencialesvendedor,
    Metodopago,
    Metodosenvio,
    Pedidos,
    Detallepedido,
    Historialbusqueda,
    Resenias
)



# Serializers
class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = "__all__"

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        exclude = ("contraseña",)  # No exponer contraseña

class VendedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedores
        exclude = ("contraseña",)

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = "__all__"

class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = "__all__"

class VentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ventas
        fields = "__all__"

class CredencialesClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CredencialesCliente
        exclude = ("contraseña",)

class CredencialesVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CredencialesVendedor
        exclude = ("contraseña",)

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = "__all__"

class MetodosEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodosEnvio
        fields = "__all__"

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = "__all__"

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = "__all__"

class HistorialBusquedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialBusqueda
        fields = "__all__"

class ReseñasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseñas
        fields = "__all__"

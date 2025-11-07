from rest_framework import serializers
from .models import (
    Ciudades, Clientes, Vendedores, Categorias, Productos,
    Estados, Ventas, Credencialescliente, Credencialesvendedor,
    Metodopago, Metodosenvio, Pedidos, Detallepedido,
    Historialbusqueda, Resenias
)

class CiudadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades
        fields = "__all__"


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"


class ProductosSerializer(serializers.ModelSerializer):
    categoria = CategoriasSerializer(read_only=True)

    class Meta:
        model = Productos
        fields = "__all__"


class ClientesSerializer(serializers.ModelSerializer):
    ciudad = CiudadesSerializer(read_only=True)

    class Meta:
        model = Clientes
        exclude = ("contrasenia",)


class VendedoresSerializer(serializers.ModelSerializer):
    ciudad = CiudadesSerializer(read_only=True)

    class Meta:
        model = Vendedores
        exclude = ("contrasenia",)


class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = "__all__"


class MetodosEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodosenvio
        fields = "__all__"


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodopago
        fields = "__all__"



class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductosSerializer(read_only=True)

    class Meta:
        model = Detallepedido
        fields = "__all__"


class PedidosSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer(read_only=True)
    metodo_envio = MetodosEnvioSerializer(read_only=True)
    metodo_pago = MetodoPagoSerializer(read_only=True)
    detalles = DetallePedidoSerializer(source="detallepedido_set", many=True, read_only=True)

    class Meta:
        model = Pedidos
        fields = "__all__"


class CredencialesClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credencialescliente
        exclude = ("contrasenia",)


class CredencialesVendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credencialesvendedor
        exclude = ("contrasenia",)


class VentasSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer(read_only=True)
    vendedor = VendedoresSerializer(read_only=True)
    producto = ProductosSerializer(read_only=True)

    class Meta:
        model = Ventas
        fields = "__all__"


class HistorialBusquedaSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer(read_only=True)
    class Meta:
        model = Historialbusqueda
        fields = "__all__"


class ReseñasSerializer(serializers.ModelSerializer):
    cliente = ClientesSerializer(read_only=True)
    producto = ProductosSerializer(read_only=True)

    class Meta:
        model = Resenias
        fields = "__all__"

from rest_framework import routers
from .views import (
    CiudadesViewSet, ClientesViewSet, VendedoresViewSet,
    CategoriasViewSet, ProductosViewSet, EstadosViewSet,
    VentasViewSet, CredencialesClienteViewSet, CredencialesVendedorViewSet,
    MetodoPagoViewSet, MetodosEnvioViewSet, PedidosViewSet,
    DetallePedidoViewSet, HistorialBusquedaViewSet, ReseñasViewSet
)

router = routers.DefaultRouter()
router.register(r'ciudades', CiudadesViewSet)
router.register(r'clientes', ClientesViewSet)
router.register(r'vendedores', VendedoresViewSet)
router.register(r'categorias', CategoriasViewSet)
router.register(r'productos', ProductosViewSet)
router.register(r'estados', EstadosViewSet)
router.register(r'ventas', VentasViewSet)
router.register(r'credencialescliente', CredencialesClienteViewSet)
router.register(r'credencialesvendedor', CredencialesVendedorViewSet)
router.register(r'metodospago', MetodoPagoViewSet)
router.register(r'metodosenvio', MetodosEnvioViewSet)
router.register(r'pedidos', PedidosViewSet)
router.register(r'detallepedido', DetallePedidoViewSet)
router.register(r'historialbusqueda', HistorialBusquedaViewSet)
router.register(r'reseñas', ReseñasViewSet)

urlpatterns = router.urls

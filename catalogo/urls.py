
from django.conf.urls import url, include
from rest_framework import routers
from .views.categoria_view import CategoriaViewSet
from .views.producto_view import ProductoViewSet
from .views.compra_view import CompraViewSet
from .views.venta_view import VentaViewSet
from .views.detalleVenta_view import DetalleVentaViewSet
from .views.detalleCompra_view import DetalleCompraViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalleVenta', DetalleVentaViewSet)
router.register(r'detalleCompra', DetalleCompraViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]

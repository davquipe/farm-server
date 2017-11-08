from django.contrib import admin
from catalogo.models.producto import Producto
from catalogo.models.unidadMed import UnidadMed
from catalogo.models.categoria import Categoria
from catalogo.models.venta import Venta
from catalogo.models.detalleVenta import DetalleVenta
from catalogo.models.cliente import Cliente
from catalogo.models.almacen import Almacen
from catalogo.models.proveedor import Proveedor
from catalogo.models.compra import Compra
from catalogo.models.detalleCompra import DetalleCompra
# Register your models here.


admin.site.register(UnidadMed)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(DetalleVenta)

admin.site.register(Almacen)
admin.site.register(Proveedor)
admin.site.register(DetalleCompra)


class ProductoAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_per_page = 2
    list_display = ("codigo", "nombre",
                    "unidad_med_codigo", "categorias", "almacen_direccion",)
    search_fields = ("codigo", "nombre",)

    def unidad_med_codigo(self, obj):
        return obj.unidad_med.codigo

    def almacen_direccion(self, obj):
        return obj.almacen.direccion

    def categorias(self, obj):
        return obj.categoria.all()

admin.site.register(Producto, ProductoAdmin)


class CompraAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_per_page = 2
    list_display = ("nro_doc", "fecha",)
    search_fields = ("nro_doc", "fecha",)

admin.site.register(Compra, CompraAdmin)


class VentaAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_per_page = 2
    list_display = ("nro_doc", "fecha",)
    search_fields = ("nro_doc", "fecha",)

admin.site.register(Venta, VentaAdmin)

from django.db import models
from .producto import Producto
from .venta import Venta


class DetalleVenta(models.Model):

    cantidad = models.IntegerField(max_length=15)
    precio_uni = models.FloatField(default=0)

    producto = models.ForeignKey(Producto)
    venta = models.ForeignKey(Venta)

    class Meta:
        verbose_name = "DetalleVenta"
        verbose_name_plural = "DetalleVentas"

    def __str__(self):
        return 'VENTA%s - PROD: %s' % (self.venta.nro_doc, self.producto.nombre,)

from django.db import models


class DetalleCompra(models.Model):

    nro_doc = models.CharField(max_length=16)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.FloatField(default=0)
    precio_unitario = models.FloatField(default=0.0)
    
    class Meta:
        verbose_name = "DetalleCompra"
        verbose_name_plural = "DetalleCompras"

    def __str__(self):
        return '%s' % (self.nro_doc)






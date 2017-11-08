from django.db import models
from .proveedor import Proveedor
from .almacen import Almacen
from core.models import User, Person

class Compra(models.Model):

    nro_doc = models.CharField(max_length=16)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.FloatField(default=0.0)
    proveedor = models.OneToOneField(Proveedor)
    almacen = models.ForeignKey(Almacen)
    comprador = models.ForeignKey(User)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return '%s' % (self.nro_doc)

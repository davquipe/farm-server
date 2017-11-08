from django.db import models
from core.models import User, Person
from .cliente import Cliente
from .almacen import Almacen


class Venta(models.Model):

    nro_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    vendedor = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    almacen = models.ForeignKey(Almacen)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.nro_doc)

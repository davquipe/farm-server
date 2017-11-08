from django.db import models
from .unidadMed import UnidadMed
from .almacen import Almacen

class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)
    fechaVen = models.DateField(auto_now_add=False)
    precio_venta = models.FloatField(default=0.0)
    unidad_med = models.ForeignKey(UnidadMed)
    almacen = models.ForeignKey(Almacen)
    categoria = models.ManyToManyField(
        "Categoria",
        verbose_name="list of Categorias",
        null=True,  blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.codigo)

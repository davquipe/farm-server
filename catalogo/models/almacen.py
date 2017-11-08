from django.db import models


class Almacen(models.Model):

    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacenes"

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.direccion,)

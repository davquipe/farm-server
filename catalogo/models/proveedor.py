from django.db import models


class Proveedor(models.Model):

    empresa = models.CharField(max_length=10)
    ruc = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return '%s (%s)' % (self.empresa, self.ruc)

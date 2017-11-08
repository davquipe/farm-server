from django.db import models


class UnidadMed(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "UnidadMed"
        verbose_name_plural = "UnidadMeds"

    def __str__(self):
        return '%s (%s)' % (self.codigo, self.nombre)

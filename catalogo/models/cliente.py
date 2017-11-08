from django.db import models
from core.models import User, Person


class Cliente(models.Model):

    ruc = models.CharField(max_length=11)
    person = models.OneToOneField(Person)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.ruc)

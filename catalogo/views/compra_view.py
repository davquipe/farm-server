from ..models.compra import Compra
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class CompraSerializer(serializers.ModelSerializer):
    almacen_nombre = serializers.SerializerMethodField()
    almacen_direccion = serializers.SerializerMethodField()

    class Meta:
        model = Compra
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_almacen_nombre(self, obj):
        return "%s " % (obj.almacen.nombre)

    def get_almacen_direccion(self, obj):
        return "%s" % (obj.almacen.direccion)


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(nro_doc__icontains=query),
                    )
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset

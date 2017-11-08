from ..models.detalleCompra import DetalleCompra
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class DetalleCompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleCompra
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(nro_doc__icontains=query),
                    Q(fecha__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset


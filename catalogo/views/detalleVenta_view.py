from ..models.detalleVenta import DetalleVenta
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class DetalleVentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleVenta
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(cantidad__icontains=query),
                    )
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset

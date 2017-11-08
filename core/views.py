from .models import User
from rest_framework import serializers, viewsets


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer

class UserCreateSerializer(UserCreateSerializer) :
    class Meta(UserCreateSerializer.Meta) : 
        model = User
        fields = ('id', 'email', 'name', 'password')

        
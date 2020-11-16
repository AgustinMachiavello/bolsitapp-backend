from rest_framework import routers, viewsets
from ..models.users import User
from ..serializers.users import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
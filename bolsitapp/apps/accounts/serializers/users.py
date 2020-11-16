from ..models.users import User
from rest_framework import serializers
from ...commerce.serializers import *

class UserSerializer(serializers.ModelSerializer):
    bags_owned = BagSerializer(read_only=True, many=True, source='user')

    class Meta:
        model = User
        exclude = ['password',]
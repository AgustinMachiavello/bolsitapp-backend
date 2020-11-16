from ..models import *
from rest_framework import serializers


class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ('__all__')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('__all__')

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ('__all__')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('__all__')
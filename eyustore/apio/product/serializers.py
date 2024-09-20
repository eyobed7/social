from rest_framework.serializers import ModelSerializer
from product.models import Product
from rest_framework import serializers

class ProductSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model=Product
        fields=('name','price','description','username')

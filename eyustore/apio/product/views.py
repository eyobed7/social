
from rest_framework import viewsets
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    permission_classes=[IsAuthenticated]
# Create your views here.

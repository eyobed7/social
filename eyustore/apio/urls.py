from rest_framework.routers import DefaultRouter
from apio.product.views import ProductViewSet
from django.urls import path,include

router=DefaultRouter()
router.register(r'', ProductViewSet, basename="product")
urlpatterns = [
    
    path('', include(router.urls)),  # Include the DRF router URLs
]
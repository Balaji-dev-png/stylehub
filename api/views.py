from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from store.models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from .serializers import CategorySerializer 
from store.models import Category

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        # Users see only their own orders
        return Order.objects.filter(user=self.request.user)




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
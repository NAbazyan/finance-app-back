from rest_framework import viewsets, permissions
from .models import Bill, Product
from .serializers import BillSerializers, ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class BillViewSets(viewsets.ModelViewSet):
    serializer_class = BillSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bill.objects.filter(account__user=self.request.user)
    
    def perform_create(self, serializer):
        account = self.request.user.accounts.first()
        serializer.save(account=account)
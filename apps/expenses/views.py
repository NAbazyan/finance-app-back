from rest_framework import viewsets, permissions
from .models import Expense
from .serializers import ExpenseSerializers


class ExpenseViewSets(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(account__user=self.request.user)
    
    def perform_create(self, serializer):
        account = self.request.user.accounts.first()
        serializer.save(account=account)
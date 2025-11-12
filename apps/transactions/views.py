from rest_framework import viewsets, permissions
from .models import Transaction
from .serialazers import TransactionSerialazer

class TransactionViewSets(viewsets.ModelViewSet):
    serializer_class = TransactionSerialazer
    permission_classes = [permissions.IsAuthenticated]
  
    def get_queryset(self):
        return Transaction.objects.filter(account__user = self.request.user)
    
    def perform_create(self, serializer):
        transaction = serializer.save()
        account = transaction.account

        if transaction.transaction_type == "credit":
            account.balance += transaction.amount
        elif transaction.transaction_type == "debit":
            account.balance -= transaction.amount
        account.save()
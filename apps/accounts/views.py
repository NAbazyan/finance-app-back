from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Account
from .serializers import AccountSerializer

class AccountViewSets(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Account.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        account = Account.objects.filter(user=request.user, id=id).first()
        if not account:
            raise NotFound("Account not found")
        
        request.user.save()

        account.delete()
        return Response({"detail": f"Account {id} deleted"},status=status.HTTP_204_NO_CONTENT)
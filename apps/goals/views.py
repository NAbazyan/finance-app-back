from rest_framework import viewsets, permissions
from .models import Goals
from .serializers import GoalsSerializers

class GoalsViewSets(viewsets.ModelViewSet):
    serializer_class = GoalsSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goals.objects.filter(account__user=self.request.user)
    
    def perform_create(self, serializer):
        account = self.request.user.accounts.first()
        serializer.save(account=account)
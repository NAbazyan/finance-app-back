from django.db import models
from apps.accounts.models import Account

class Goals(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='goals')
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monthly_target = models.DecimalField(max_digits=10, decimal_places=2)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    
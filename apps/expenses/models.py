from django.db import models
from apps.accounts.models import Account

class Expense(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='expense')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - ${self.amount}"
    
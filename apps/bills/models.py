from django.db import models
from apps.accounts.models import Account


class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    logo = models.URLField()

    def __str__(self):
        return self.title

class Bill(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="bills")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="bills")
    due_date = models.DateField()
    last_charge = models.DateField()
    des_name = models.CharField(max_length=50, default='', null=True)
    description = models.CharField(max_length=200, default='', null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['due_date']
        
    def __str__(self):
        return f"{self.product} - ${self.amount}"
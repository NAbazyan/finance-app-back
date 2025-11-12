from django.db import models
from apps.accounts.models import Account

class Transaction(models.Model):
    PAYMENT_METHODS = (
        ('creditcard', "Credit Card"),
    )

    TRANSACTION_TYPES = (
        ("debit", "Debit"),
        ("credit", "Credit")  
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default="debit")
    shop_name = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    items = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    category = models.CharField(max_length=150, default="others")

    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return f"{self.shop_name} - {self.amount} ({self.payment_method})"
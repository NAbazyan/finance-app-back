from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Account(models.Model):
    ACCOUNT_TYPES = (
        ('creditcard', "Credit Card"),
        ('checking', "Checking"),
        ('savings', "Savings"),
        ('investment', "Investment"),
        ('loan', "Loan"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    bank_name = models.CharField(max_length=100)
    bank_short = models.CharField(max_length=100, default="")
    branch_name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    account_number = models.CharField(max_length=50, unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)


    def __str__(self):
        return f"{self.bank_name} ({self.account_type} - {self.account_number})"
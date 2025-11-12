from rest_framework import serializers
from .models import Transaction

class TransactionSerialazer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            "id",
            "account",
            "shop_name",
            "amount",
            "items",
            "date",
            "payment_method",
            "transaction_type",
            "category"
        ]
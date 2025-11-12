from rest_framework import serializers
from .models import Expense

class ExpenseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = [
            "title",
            "amount",
            "category",
            "date",
        ]

        read_only_fields =  [
            "account",
            "date"
        ]
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "id",
            "account_number",
            "account_type",
            "branch_name",
            "bank_short",
            "bank_name",
            "balance",
        ]
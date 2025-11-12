from rest_framework import serializers
from .models import Goals

class GoalsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Goals
        fields = [
            "account",
            "current_amount",
            "monthly_target",
            "target_amount",
            "title",
            "created_at"
        ]
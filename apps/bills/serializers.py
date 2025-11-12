from rest_framework import serializers
from .models import Bill, Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "logo"
        ]

class BillSerializers(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source="product",
        write_only=True
    )

    class Meta:
        model = Bill
        fields = [
            "id",
            "account",
            "product",
            "product_id",
            "due_date",
            "last_charge",
            "des_name",
            "description",
            "amount",
            "created_at",
            "updated_at"
        ]
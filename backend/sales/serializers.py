from rest_framework import serializers
from django.db import transaction

from .models import Sale, SaleItem
from .services import SaleService


class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        exclude = ("sale",)


class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)

    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = (
            "subtotal",
            "gst_amount",
            "grand_total",
        )

    @transaction.atomic
    def create(self, validated_data):

        items_data = validated_data.pop("items")

        sale = Sale.objects.create(**validated_data)

        for item_data in items_data:

            SaleItem.objects.create(
                sale=sale,
                **item_data,
            )

        SaleService.update_stock(sale)

        return sale
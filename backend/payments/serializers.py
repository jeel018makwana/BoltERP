from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"

    def validate(self, attrs):
        payment_type = attrs.get("payment_type")
        customer = attrs.get("customer")
        supplier = attrs.get("supplier")

        if payment_type == "RECEIVED" and not customer:
            raise serializers.ValidationError(
                "Customer is required for received payments."
            )

        if payment_type == "PAID" and not supplier:
            raise serializers.ValidationError(
                "Supplier is required for paid payments."
            )

        return attrs
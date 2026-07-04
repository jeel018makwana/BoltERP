from rest_framework import serializers
from .models import Customer
import re


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"

    def validate_name(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError(
                "Customer name must be at least 2 characters."
            )

        return value

    def validate_phone(self, value):

        if not re.fullmatch(r"[6-9]\d{9}", value):
            raise serializers.ValidationError(
                "Enter a valid 10-digit Indian mobile number."
            )

        return value

    def validate_gst_number(self, value):

        if value:
            pattern = r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{3}$"

            if not re.fullmatch(pattern, value):
                raise serializers.ValidationError(
                    "Invalid GST Number."
                )

        return value

    def validate_opening_balance(self, value):

        if value < 0:
            raise serializers.ValidationError(
                "Opening balance cannot be negative."
            )

        return value

    def validate_pincode(self, value):

        if value:

            if not re.fullmatch(r"\d{6}", value):
                raise serializers.ValidationError(
                    "Pincode must be 6 digits."
                )

        return value
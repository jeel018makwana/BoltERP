from rest_framework import serializers
from .models import Category, Brand, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    brand_name = serializers.CharField(
        source="brand.name",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = "__all__"

    # ---------- Field Validations ----------

    def validate_name(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError(
                "Product name must contain at least 2 characters."
            )
        return value

    def validate_purchase_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Purchase price cannot be negative."
            )
        return value

    def validate_selling_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Selling price must be greater than 0."
            )
        return value

    def validate_gst(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError(
                "GST must be between 0 and 100."
            )
        return value

    def validate_current_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Current stock cannot be negative."
            )
        return value

    # ---------- Object Validation ----------

    def validate(self, attrs):

        purchase_price = attrs.get("purchase_price")
        selling_price = attrs.get("selling_price")

        if (
            purchase_price is not None
            and selling_price is not None
            and selling_price < purchase_price
        ):
            raise serializers.ValidationError(
                {
                    "selling_price":
                        "Selling price should not be less than purchase price."
                }
            )

        return attrs
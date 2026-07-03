from decimal import Decimal

from django.db import transaction

from inventory.models import InventoryTransaction


class PurchaseService:

    @staticmethod
    @transaction.atomic
    def update_stock(purchase):

        subtotal = Decimal("0.00")
        total_gst = Decimal("0.00")

        for item in purchase.items.all():

            # Calculate Item Total
            basic_amount, gst_amount = item.calculate_total()

            item.save(update_fields=["line_total"])

            subtotal += basic_amount
            total_gst += gst_amount

            # Update Product Stock
            product = item.product
            product.current_stock += item.quantity
            product.save(update_fields=["current_stock"])

            # Inventory Entry
            InventoryTransaction.objects.create(
                product=product,
                transaction_type="PURCHASE",
                quantity=item.quantity,
                reference=purchase.purchase_number,
                remarks="Stock added through Purchase",
            )

        # Update Purchase Totals
        purchase.subtotal = subtotal
        purchase.gst_amount = total_gst

        purchase.grand_total = (
            subtotal +
            total_gst -
            purchase.discount
        )

        purchase.save(
            update_fields=[
                "subtotal",
                "gst_amount",
                "grand_total",
            ]
        )
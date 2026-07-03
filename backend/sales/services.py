from django.db import transaction
from products.models import Product


class SaleService:

    @staticmethod
    @transaction.atomic
    def update_stock(sale):

        subtotal = 0
        gst_total = 0

        for item in sale.items.all():

            product = item.product

            if product.current_stock < item.quantity:
                raise ValueError(
                    f"Insufficient stock for {product.name}"
                )

            product.current_stock -= item.quantity
            product.save()

            line_total = item.quantity * item.selling_price

            item.line_total = line_total
            item.save()

            subtotal += line_total
            gst_total += (line_total * item.gst) / 100

        sale.subtotal = subtotal
        sale.gst_amount = gst_total
        sale.grand_total = subtotal + gst_total - sale.discount

        sale.save()
from django.db import models
from common.models import TimeStampedModel
from suppliers.models import Supplier
from products.models import Product
from django.conf import settings


class Purchase(TimeStampedModel):

    purchase_number = models.CharField(
        max_length=30,
        unique=True,
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="purchases",
    )

    invoice_number = models.CharField(
        max_length=100,
    )

    purchase_date = models.DateField()

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    gst_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    grand_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    remarks = models.TextField(
        blank=True,
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ["-purchase_date"]

    def __str__(self):
        return self.purchase_number


class PurchaseItem(TimeStampedModel):

    purchase = models.ForeignKey(
        Purchase,
        on_delete=models.CASCADE,
        related_name="items",
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )

    quantity = models.PositiveIntegerField()

    purchase_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    gst = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18,
    )

    line_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.product.name
    
    def calculate_total(self):
        """
        Calculates line total including GST.
        """

        basic_amount = self.quantity * self.purchase_price

        gst_amount = (basic_amount * self.gst) / 100

        self.line_total = basic_amount + gst_amount

        return basic_amount, gst_amount
from django.db import models
from common.models import TimeStampedModel


class Supplier(TimeStampedModel):
    supplier_code = models.CharField(
        max_length=20,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    company_name = models.CharField(
        max_length=200,
        blank=True,
    )

    phone = models.CharField(
        max_length=20,
    )

    email = models.EmailField(
        blank=True,
    )

    gst_number = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    city = models.CharField(
        max_length=100,
        blank=True,
    )

    state = models.CharField(
        max_length=100,
        blank=True,
    )

    pincode = models.CharField(
        max_length=10,
        blank=True,
    )

    opening_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.supplier_code} - {self.name}"
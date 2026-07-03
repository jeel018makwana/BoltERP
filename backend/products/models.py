from django.db import models
from common.models import TimeStampedModel


class Category(TimeStampedModel):
    """
    Product Category
    Example:
        Bolt
        Nut
        Washer
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(TimeStampedModel):
    """
    Product Brand
    Example:
        TVS
        Unbrako
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    """
    Product Master
    """

    product_code = models.CharField(
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        max_length=200,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name="products",
    )

    grade = models.CharField(
        max_length=50,
        blank=True,
    )

    material = models.CharField(
        max_length=100,
        blank=True,
    )

    size = models.CharField(
        max_length=100,
        blank=True,
    )

    unit = models.CharField(
        max_length=20,
        default="PCS",
    )

    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    gst = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=18,
    )

    current_stock = models.IntegerField(
        default=0,
    )

    minimum_stock = models.IntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.product_code} - {self.name}"
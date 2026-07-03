from django.contrib import admin
from .models import InventoryTransaction


@admin.register(InventoryTransaction)
class InventoryTransactionAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "transaction_type",
        "quantity",
        "reference",
        "created_at",
    )

    search_fields = (
        "product__name",
        "reference",
    )

    list_filter = (
        "transaction_type",
    )

    ordering = (
        "-created_at",
    )
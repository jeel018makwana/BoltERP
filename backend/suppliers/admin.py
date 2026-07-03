from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        "supplier_code",
        "name",
        "phone",
        "city",
        "opening_balance",
        "is_active",
    )

    search_fields = (
        "supplier_code",
        "name",
        "phone",
    )

    list_filter = (
        "city",
        "is_active",
    )

    ordering = (
        "name",
    )
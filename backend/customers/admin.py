from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_code",
        "name",
        "phone",
        "city",
        "opening_balance",
        "is_active",
    )

    search_fields = (
        "customer_code",
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
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "payment_number",
        "payment_date",
        "payment_type",
        "customer",
        "supplier",
        "amount",
        "payment_mode",
    )

    list_filter = (
        "payment_type",
        "payment_mode",
        "payment_date",
    )

    search_fields = (
        "payment_number",
        "customer__name",
        "supplier__name",
    )
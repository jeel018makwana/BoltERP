from django.contrib import admin
from .models import Purchase, PurchaseItem


class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):

    list_display = (
        "purchase_number",
        "supplier",
        "purchase_date",
        "grand_total",
        "created_by",
    )

    search_fields = (
        "purchase_number",
        "invoice_number",
        "supplier__name",
    )

    list_filter = (
        "purchase_date",
        "supplier",
    )

    inlines = [
        PurchaseItemInline,
    ]

    def save_related(self, request, form, formsets, change):

        super().save_related(request, form, formsets, change)

        if not change:
            from .services import PurchaseService
            PurchaseService.update_stock(form.instance)



@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):

    list_display = (
        "purchase",
        "product",
        "quantity",
        "purchase_price",
        "line_total",
    )

    search_fields = (
        "purchase__purchase_number",
        "product__name",
    )
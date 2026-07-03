from django.contrib import admin
from .models import Sale, SaleItem
from .services import SaleService


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):

    list_display = (
        "sale_number",
        "customer",
        "sale_date",
        "grand_total",
    )

    inlines = [SaleItemInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        SaleService.update_stock(form.instance)
from rest_framework import filters, viewsets

from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        "supplier_code",
        "name",
        "phone",
        "company_name",
    ]
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Sale
from .serializers import SaleSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .pdf import generate_invoice
from .models import Sale

class SaleViewSet(viewsets.ModelViewSet):

    queryset = Sale.objects.prefetch_related(
        "items__product"
    ).select_related(
        "customer",
        "created_by",
    )

    serializer_class = SaleSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class InvoicePDFAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        sale = get_object_or_404(
            Sale.objects.prefetch_related(
                "items__product"
            ).select_related(
                "customer"
            ),
            pk=pk,
        )

        pdf = generate_invoice(sale)

        response = HttpResponse(
            pdf,
            content_type="application/pdf"
        )

        response["Content-Disposition"] = (
            f'attachment; filename="Invoice_{sale.sale_number}.pdf"'
        )

        return response
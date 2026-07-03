from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, InvoicePDFAPIView
router = DefaultRouter()
router.register("", SaleViewSet, basename="sales")

urlpatterns = [

    path(
        "<int:pk>/invoice/",
        InvoicePDFAPIView.as_view(),
        name="sale-invoice",
    ),

    path("", include(router.urls)),
]
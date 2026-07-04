from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Brand, Product
from .serializers import (
    CategorySerializer,
    BrandSerializer,
    ProductSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from logs.utils import log_activity

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.select_related(
        "category",
        "brand",
    )

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_class = ProductFilter

    search_fields = [
        "product_code",
        "name",
        "grade",
        "size",
        "material",
    ]

    ordering_fields = [
        "name",
        "selling_price",
        "purchase_price",
        "current_stock",
    ]

    ordering = [
        "name",
    ]

    def perform_create(self, serializer):
        product = serializer.save()

        log_activity(
            user=self.request.user,
            action = "CREATE",
            description =f"Created product: {product.name}",
        )

    def perform_update(self, serializer):
        product = serializer.save()

        log_activity(
            user=self.request.user,
            action="UPDATE",
            module="Products",
            description=f"Updated product: {product.name}",
        )

    def perform_destroy(self, instance):
        log_activity(
            user=self.request.user,
            action="DELETE",
            module="Products",
            description=f"Deleted products: {instance.name}",
        )
        instance.delete()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]

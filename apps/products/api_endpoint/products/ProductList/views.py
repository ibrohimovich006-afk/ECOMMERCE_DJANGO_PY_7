from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.products.api_endpoint.products.ProductList.serializer import ProductListSerializer
from apps.products.api_endpoint.products.filters import ProductFilter
from apps.products.models import Product
from apps.orders.pagination import CustomLimitOffsetPagination


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomLimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
from django_filters import FilterSet, CharFilter
from apps.products.models import Product


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    price_gte = CharFilter(field_name='price', lookup_expr='gte')
    price_lte = CharFilter(field_name='price', lookup_expr='lte')


    class Meta:
        model = Product
        fields = ['category', 'price_gte', 'price_lte', 'name']
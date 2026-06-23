from django_filters import FilterSet, CharFilter
from apps.orders.models import Order



class OrderFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    price_gte = CharFilter(field_name='price', lookup_expr='gte')
    price_lte = CharFilter(field_name='price', lookup_expr='lte')


    class Meta:
        model = Order
        fields = ['category', 'price_gte', 'price_lte', 'name']
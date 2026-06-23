from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from apps.orders.api_endpoint.orders.OrdersList.serializer import OrderListSerializer
from apps.orders.models import Order


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderListSerializer(orders, many=True)
    return Response(serializer.data)


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status='Yangi')
        return queryset
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.api_endpoint.orders.OrderDetail.serializer import OrderDetailSerializer
from apps.orders.models import Order


@api_view(['GET'])
def order_detail_view(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

    serializer = OrderDetailSerializer(order)
    return Response(serializer.data)
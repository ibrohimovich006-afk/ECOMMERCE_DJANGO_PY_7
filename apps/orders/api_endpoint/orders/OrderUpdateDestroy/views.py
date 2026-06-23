from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView

from apps.orders.api_endpoint.orders.OrderUpdateDestroy.serializer import OrderUpdateSerializer
from apps.orders.models import Order


@api_view(['PATCH', 'DELETE'])
def order_update_destroy(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=404)

    if request.method == 'PATCH':
        serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderUpdateSerializer(order).data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=204)
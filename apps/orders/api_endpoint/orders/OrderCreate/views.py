from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from apps.orders.api_endpoint.orders.OrderCreate.serializer import OrderCreateSerializer
from apps.orders.models import Order


@api_view(['POST'])
def order_create(request):
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response(OrderCreateSerializer(order).data, status=201)
    return Response(serializer.errors, status=400)


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
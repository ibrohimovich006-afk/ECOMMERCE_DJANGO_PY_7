from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.api_endpoint.products.ProductCreate.serializer import ProductCreateSerializer


@api_view(['POST'])
def product_create(request):
    serializer = ProductCreateSerializer(data=request.data)

    if serializer.is_valid():
        product = serializer.save()
        return Response(
            ProductCreateSerializer(product).data,
            status=201
        )

    return Response(serializer.errors, status=400)
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.api_endpoint.products.ProductDetail.serializer import ProductDetailSerializer


@api_view(['GET'])
def product_detail_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)
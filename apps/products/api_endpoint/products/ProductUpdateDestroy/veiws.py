from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.api_endpoint.products.ProductUpdateDestroy.serializer import ProductUpdateSerializer


@api_view(['PATCH', 'DELETE'])
def product_update_destroy_view(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    if request.method == 'PATCH':
        serializer = ProductUpdateSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductUpdateSerializer(product).data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=204)
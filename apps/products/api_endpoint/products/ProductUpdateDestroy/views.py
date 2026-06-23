from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.products.api_endpoint.products.ProductUpdateDestroy.serializer import ProductUpdateSerializer
from apps.products.models import Product

@extend_schema(request=ProductUpdateSerializer(partial=True),responses={200: ProductUpdateSerializer})
@api_view(['PATCH'])
def product_update(request,pk):
    try:
        product = Product.objects.get(id=pk)
    except:
        return Response('Product not found',status=400)
    
    serializer = ProductUpdateSerializer(product,request.data,partial=True)
    if serializer.is_valid():
        product = serializer.save()
        return Response(ProductUpdateSerializer(product).data,status=201)
    return Response(serializer.errors,status=400)
    



@api_view(['DELETE'])
def product_destroy(request,pk):
    try:
        product = Product.objects.get(id=pk)
    except:
        return Response('Product not found',status=400)
    
    product.delete()
    return Response(status=204)
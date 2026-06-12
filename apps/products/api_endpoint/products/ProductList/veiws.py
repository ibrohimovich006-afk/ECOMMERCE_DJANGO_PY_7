from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from apps.products.api_endpoint.products.ProductList.serializer import ProductListSerializer 
from apps.products.models import Product

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly]) 
def product_list(request):
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)
   


from django.urls import path
from apps.products.api_endpoint.products.ProductList.veiws import product_list

urlpatterns = [ path('', product_list, name='product_list'), ]
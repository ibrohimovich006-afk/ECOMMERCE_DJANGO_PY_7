from django.urls import path

from apps.products.api_endpoint.products.ProductList.views import ProductListView
from apps.products.api_endpoint.products.ProductDetail.views import product_detail
from apps.products.api_endpoint.products.ProductCreate.views import product_create
from apps.products.api_endpoint.products.ProductUpdateDestroy.views import product_update,product_destroy


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/update/', product_update, name='product_update'),
    path('<int:pk>/delete/', product_destroy, name='product_delete'),
]
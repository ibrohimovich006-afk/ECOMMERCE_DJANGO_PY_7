from django.urls import path
from apps.orders.api_endpoint.orders.OrderDetail.views import order_detail
from apps.orders.api_endpoint.orders.OrderUpdateDestroy.views import order_update_destroy
from apps.orders.api_endpoint.orders.OrderCreate.views import order_create
from apps.orders.api_endpoint.orders.OrdersList.views import order_list

urlpatterns = [
    path('', order_list, name='order-list'),
    path('create/', order_create, name='order-create'),
    path('<int:pk>/', order_detail, name='order-detail'),
    path('<int:pk>/update/', order_update_destroy, name='order-update'),
    path('<int:pk>/delete/', order_update_destroy, name='order-delete'),
]
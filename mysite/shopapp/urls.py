from django.urls import path
from .views import *

app_name='shopapp'

urlpatterns = [
    path("", index, name='shopapp-index'),
    path("groups", get_groups, name='get-groups'),
    path("products", get_products, name='get-products'),
    path("orders", get_orders, name='get-orders'),
]
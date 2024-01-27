from django.urls import path
from .views import *

app_name='shopapp'

urlpatterns = [
    path("", ShopView.as_view(), name='shopapp-index'),
    path("groups/", GroupView.as_view(), name='get-groups'),
    path("products/", get_products, name='get-products'),
    path("products/create/", create_product, name='create-products'),
    path("orders", get_orders, name='get-orders'),
]
from django.urls import include, path
from .views import *
from rest_framework.routers import DefaultRouter

app_name='shopapp'

routers = DefaultRouter()
routers.register('products', ProductViewSet)

urlpatterns = [
    path("", ShopView.as_view(), name='shopapp-index'),
    path("groups/", GroupView.as_view(), name='get-groups'),
    path("products/", ProductsListView.as_view(), name='get-products'),
    path("products/create/", ProductCreateView.as_view(), name='create-products'),
    path("products/<int:pk>/", ProductDetailView.as_view(), name='product-detail'),
    path("products/<int:pk>/edit", ProductUpdateView.as_view(), name='product-edit'),
    path("products/<int:pk>/confirm-delete", ProductConfirmDeleteView.as_view(), name='product-confirm-delete'),
    path("orders/", OrderListView.as_view(), name='get-orders'),
    path("orders/<int:pk>", OrderDetailView.as_view(), name='order-detail'),
    path("api/", include(routers.urls))
]
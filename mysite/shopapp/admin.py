from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import Order, Product


class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    list_display = 'pk', 'name', 'short_description', 'price', 'discount'
    list_display_links = 'pk', 'name'
    ordering = 'name',
    search_fields = 'name', 'description'

    def short_description(self, obj: Product)->str:
        if(len(obj.description) < 30):
            return obj.description
        else:
            return obj.description[:30] + '...'
        

class ProductInline(admin.TabularInline):
    model = Order.products.through

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbose'

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return Order.objects.select_related('user')
    
    def user_verbose(self, obj: Order):
        return obj.user.first_name or obj.user.username
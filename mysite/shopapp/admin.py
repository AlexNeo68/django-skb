from csv import DictReader
from io import TextIOWrapper
from os import error
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.urls import path
from django.urls.resolvers import URLPattern

from .forms import ImportCSVForm

from .admin_mixins import ExportAsCSVMixin

from .models import Order, Product, ProductImage


class OrderInline(admin.TabularInline):
    model = Product.orders.through

class ProductImageInline(admin.StackedInline):
    model = ProductImage

@admin.action(description='Архивировать товары')
def archive(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description='Разархивировать товары')
def unarchive(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    change_list_template = 'shopapp/admin-products-change_list.html'
    actions = [archive, unarchive, 'export_csv']
    inlines = [OrderInline, ProductImageInline]
    list_display = 'pk', 'name', 'short_description', 'price', 'discount', 'archived'
    list_display_links = 'pk', 'name'
    ordering = 'name',
    search_fields = 'name', 'description'
    fieldsets = [
        (
            None, {
                "fields": ['name', 'description']
            },
            
        ),
        (
            "Images", {
                "fields": ['preview'],
                "classes": ['wide']
            }
        ),
        (
            "Shop Options", {
                "fields": ['price', 'discount'],
                "classes": ['collapse', 'wide']
            }
        ),
        (
            "Extra", {
                "fields": ['archived'],
                "classes": ['collapse'],
                "description": "This field for soft delete"
            }
        )
    ]

    def short_description(self, obj: Product)->str:
        if(len(obj.description) < 30):
            return obj.description
        else:
            return obj.description[:30] + '...'
        
    def import_csv(self, request: HttpRequest):
        if request.method == 'GET':
            form = ImportCSVForm()
            context = {
                'form': form
            }
            return render(request, 'admin/import_csv.html', context)
        form = ImportCSVForm(request.POST, request.FILES)

        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'admin/import_csv.html', context, status=400)
        
        csv_file = TextIOWrapper(
            form.files['csv_file'].file,
            encoding=request.encoding
        )
        reader = DictReader(csv_file)
        products = [
            Product(**row)
            for row in reader
        ]
        Product.objects.bulk_create(products)
        self.message_user(request, 'Data from CSV was imported')
        return redirect('..')



    def get_urls(self):
        urls = [
            path('import-csv/', self.import_csv, name='admin-import-product-from-csv')
        ]
        return urls + super().get_urls()
        

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
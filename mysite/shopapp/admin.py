from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'short_description', 'price', 'discount'
    list_display_links = 'pk', 'name'
    ordering = 'name',
    search_fields = 'name', 'description'

    def short_description(self, obj: Product)->str:
        if(len(obj.description) < 30):
            return obj.description
        else:
            return obj.description[:30] + '...'
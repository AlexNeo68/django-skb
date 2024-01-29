from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'pk', 'name', 'description', 'preview', 'price', 'discount', 'archived', 'created_at'
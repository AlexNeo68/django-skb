from django.forms import ModelForm
from .models import Product

class ProductFormCreate(ModelForm):
    
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount"

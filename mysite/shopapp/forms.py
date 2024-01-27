from django.forms import ModelForm
from .models import Product
from django.contrib.auth.models import Group

class ProductFormCreate(ModelForm):
    
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount"

class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = 'name',

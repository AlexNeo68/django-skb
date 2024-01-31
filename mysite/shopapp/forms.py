from django import forms
from .models import Product
from django.contrib.auth.models import Group

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "name", "description", "price", "discount", 'preview'
    
    images = forms.ImageField(widget=forms.ClearableFileInput())

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = 'name',

class ImportCSVForm(forms.Form):
    csv_file = forms.FileField()

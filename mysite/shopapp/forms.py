from django import forms

class ProductFormCreate(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=8, max_value=1000)
    discount = forms.IntegerField(min_value=0, required=False)
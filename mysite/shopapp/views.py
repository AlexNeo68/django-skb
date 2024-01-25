from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView


def index(request:HttpRequest):
    products = [
        ('Iphone', '1999'),
        ('iMac', '2999'),
        ('MacPro', '1500'),
    ]
    context = {
        'products': products
    }
    return render(request, 'shopapp/index.html', context)

class ShopIndexView(ListView):
    template_name = 'shopapp/index.html'

from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import Group

from .forms import GroupForm, ProductFormCreate

from .models import Order, Product

class ShopView(View):
    def get(self, request:HttpRequest):
        products = [
            ('Iphone', '1999'),
            ('iMac', '2999'),
            ('MacPro', '1500'),
        ]
        context = {
            'products': products
        }
        return render(request, 'shopapp/index.html', context)


class GroupView(View):
    def get(self, request: HttpRequest):
        context = {
            'groups': Group.objects.prefetch_related('permissions').all(),
            'form': GroupForm()
        }
        return render(request, 'shopapp/groups-list.html', context)
    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shopapp:get-groups')

    


def get_products(request: HttpRequest):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shopapp/products-list.html', context)

def create_product(request: HttpRequest):
    if request.method == "POST":
        form = ProductFormCreate(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('shopapp:get-products')
            return redirect(url)
    else: 
        form = ProductFormCreate()
        
    context = {
        'form': form
    }
    return render(request, 'shopapp/products-create.html', context)

def get_orders(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(request, 'shopapp/orders-list.html', context)
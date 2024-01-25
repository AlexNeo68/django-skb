from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView


def index(request:HttpRequest):
    return render(request, 'shopapp/index.html')

class ShopIndexView(ListView):
    template_name = 'shopapp/index.html'

from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import Group


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

def get_groups(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all()
    }
    return render(request, 'shopapp/groups-list.html', context)

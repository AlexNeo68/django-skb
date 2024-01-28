from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
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

    
class ProductsListView(ListView):
    template_name = 'shopapp/products-list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(archived=False)


class ProductDetailView(DetailView):
    # model = Product
    template_name = 'shopapp/product-detail.html'
    context_object_name = 'product'
    queryset = Product.objects.filter(archived=False)

class ProductCreateView(CreateView):
    model = Product
    fields = 'name', 'description', 'price', 'discount'
    success_url = reverse_lazy('shopapp:get-products')

# def create_product(request: HttpRequest):
#     if request.method == "POST":
#         form = ProductFormCreate(request.POST)
#         if form.is_valid():
#             form.save()
#             url = reverse('shopapp:get-products')
#             return redirect(url)
#     else: 
#         form = ProductFormCreate()
        
#     context = {
#         'form': form
#     }
#     return render(request, 'shopapp/products-create.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = 'name', 'description', 'price', 'discount'
    def get_success_url(self):
        return self.object.get_absolute_url()

class ProductConfirmDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:get-products')

    def form_valid(self, form):
        success_url = self.get_success_url()
        # self.object.delete()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrderListView(ListView):
    queryset= (Order.objects.select_related('user').prefetch_related('products'))
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    queryset= (Order.objects.select_related('user').prefetch_related('products'))
    context_object_name = 'order'
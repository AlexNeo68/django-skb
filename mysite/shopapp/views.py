import logging
from django.contrib.admin import action
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .serializer import ProductSerializer

from .forms import GroupForm, ProductForm

from .models import Order, Product, ProductImage

from rest_framework import filters
from rest_framework.request import Request

from django_filters.rest_framework import DjangoFilterBackend

from django.views.decorators.cache import cache_page

class ProductViewSet(ModelViewSet):
    """
    Полный CRUD операций с моделью Product
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter] 
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'description', 'price']

    filterset_fields = ['name', 'description', 'price', 'discount', 'archived']

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        print('bez cache')
        return super().list(request, *args, **kwargs)


class ShopView(View):
    def get(self, request:HttpRequest):
        
        log = logging.getLogger(__name__)

        products = [
            ('Iphone', '1999'),
            ('iMac', '2999'),
            ('MacPro', '1500'),
        ]
        context = {
            'products': products
        }

        log.debug('Products for shop index - %s', products)
        log.info('Products for shop index - %s', products)

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
    queryset = Product.objects.filter(archived=False).prefetch_related('images')





class ProductCreateView(UserPassesTestMixin, CreateView):
    def test_func(self) -> bool | None:
        return self.request.user.is_superuser
    
    model = Product
    fields = 'name', 'description', 'price', 'discount', 'preview',
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
    # fields = 'name', 'description', 'price', 'discount', 'preview',
    form_class = ProductForm
    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(image=image, product=self.object)

        return response

class ProductConfirmDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:get-products')

    def form_valid(self, form):
        success_url = self.get_success_url()
        # self.object.delete()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrderListView(LoginRequiredMixin, ListView):
    queryset= (Order.objects.select_related('user').prefetch_related('products'))
    context_object_name = 'orders'

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shopapp.view_order'
    queryset= (Order.objects.select_related('user').prefetch_related('products'))
    context_object_name = 'order'
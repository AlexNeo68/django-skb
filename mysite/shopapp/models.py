from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


def gen_product_preview_directory_name(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/preview/{filename}".format(pk=instance.pk, filename=filename)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
    preview = models.ImageField(blank=True, null=True, upload_to=gen_product_preview_directory_name)

    def get_absolute_url(self):
        return reverse("shopapp:product-detail", kwargs={"pk": self.pk})
    

    class Meta:
        ordering = ['name']
        verbose_name = _('Товар')
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
    
    @property
    def short_description(self)->str:
        if(len(self.description) < 48):
            return self.description
        else:
            return self.description[:48] + '...'
        

def gen_product_images_directory_name(instance: "Product", filename: str) -> str:
    return "products/product_{pk}/images/{filename}".format(pk=instance.product.pk, filename=filename)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=gen_product_images_directory_name)

class Order(models.Model):
    delivery_address = models.TextField(blank=True, null=True)
    promocode = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')
    reciept = models.FileField(null=True, upload_to="orders/receipts/")

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def get_absolute_url(self):
        return reverse("shopapp:order-detail", kwargs={"pk": self.pk})
    


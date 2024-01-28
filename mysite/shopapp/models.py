from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("shopapp:product-detail", kwargs={"pk": self.pk})
    

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
    
    @property
    def short_description(self)->str:
        if(len(self.description) < 48):
            return self.description
        else:
            return self.description[:48] + '...'
    

class Order(models.Model):
    delivery_address = models.TextField(blank=True, null=True)
    promocode = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='orders')

    def get_absolute_url(self):
        return reverse("shopapp:order-detail", kwargs={"pk": self.pk})
    


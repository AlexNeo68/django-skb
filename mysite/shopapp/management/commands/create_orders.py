from typing import Any, Sequence
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Order, Product


class Command(BaseCommand):

    @transaction.atomic
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('Creating orders')

        user = User.objects.get(username='admin')

        products:Sequence[Product] = Product.objects.all()

        order, created = Order.objects.get_or_create(
            delivery_address='Кремль1', 
            promocode='ORDER321', 
            user=user,
            )
        
        for product in products:
            order.products.add(product)
        
        order.save()

        self.stdout.write(f'Created Order {order}')
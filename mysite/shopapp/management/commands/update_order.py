from typing import Any
from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('Updating order')

        order = Order.objects.first()
        if not order:
            self.stdout.write(self.style.ERROR('Order not found'))

        for product in Product.objects.all():
            order.products.add(product)        

        self.stdout.write(self.style.SUCCESS(f'Update order - {order} with products {order.products}'))
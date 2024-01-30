from typing import Any
from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write(self.style.WARNING('Selecting fields'))


        info = [
            ('Smartphone 1', 199),
            ('Smartphone 2', 299),
            ('Smartphone 3', 399),
        ]

        products = [
            Product(name=name, price=price) for name, price in info
        ]
        
        result = Product.objects.bulk_create(products)

        print(result)

        self.stdout.write(self.style.SUCCESS(f'done'))
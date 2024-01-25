from typing import Any
from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('Creating products')

        product_names = [
            'iPhone', 'iMac', 'Makbook Pro'
        ]

        for product_name in product_names:
            product, created = Product.objects.get_or_create(name=product_name)
            self.stdout.write(f'Create product name is {{product}}')
        

        self.stdout.write(self.style.SUCCESS('all fine!'))
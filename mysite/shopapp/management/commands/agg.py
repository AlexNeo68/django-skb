from typing import Any
from django.core.management import BaseCommand
from django.db.models import Avg, Count, Max, Sum

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write(self.style.WARNING('Aggregate & annotate'))

# aggregate
        # result = Product.objects.aggregate(average_price=Avg('price'), maximum_price=Max('price'), maximum_discount=Max('discount'))

        # results = Order.objects.annotate(products_total_summ=Sum('products__price'))
        # for res in results:
        #     print(
        #         f'Order # {res.pk} contain product total sum {res.products_total_summ}' 
        #     )


        results = Product.objects.annotate(count_orders=Count('orders__pk')).filter(count_orders__gt=0)

        for res in results:
            print(f'Product {res.name} include in {res.count_orders} order')

        self.stdout.write(self.style.SUCCESS(f'done'))
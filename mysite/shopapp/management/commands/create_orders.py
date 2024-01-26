from typing import Any
from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write('Creating orders')

        user = User.objects.get(username='admin')

        
        order = Order.objects.get_or_create(
            delivery_address='Кремль 55', 
            promocode='ORDER123', 
            user=user,
            )

        self.stdout.write(f'Created Order {order}')
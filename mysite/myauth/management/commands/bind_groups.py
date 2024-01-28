from typing import Any
from django.core.management import BaseCommand
from django.contrib.auth.models import User, Group, Permission

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        user = User.objects.get(pk=2)
        group, created = Group.objects.get_or_create(name='profile_managers')
        user.groups.add(group)
        
        permission_view_profile = Permission.objects.get(codename='view_profile')
        group.permissions.add(permission_view_profile)

        permission_view_logentry = Permission.objects.get(codename='view_logentry')
        user.user_permissions.add(permission_view_logentry)
        
        group.save()
        user.save()      

        self.stdout.write(self.style.SUCCESS(f'{user} updated')) 
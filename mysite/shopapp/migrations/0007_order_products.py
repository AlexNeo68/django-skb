# Generated by Django 5.0.1 on 2024-01-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0006_rename_deliver_address_order_delivery_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(related_name="products", to="shopapp.product"),
        ),
    ]

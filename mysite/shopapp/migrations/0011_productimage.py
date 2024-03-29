# Generated by Django 5.0.1 on 2024-01-29 06:33

import django.db.models.deletion
import shopapp.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0010_product_preview"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        upload_to=shopapp.models.gen_product_images_directory_name
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="shopapp.product",
                    ),
                ),
            ],
        ),
    ]

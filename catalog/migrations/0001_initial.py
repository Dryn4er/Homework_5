# Generated by Django 5.1.5 on 2025-02-08 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название продукта"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание продукта"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name", "description"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "name",
                    models.CharField(max_length=150, verbose_name="Название продукта"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание продукта"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="", verbose_name="Изображение продукта"
                    ),
                ),
                (
                    "category",
                    models.CharField(max_length=150, verbose_name="Категория продукта"),
                ),
                (
                    "price",
                    models.FloatField(
                        help_text="Введите стоимость продукта",
                        verbose_name="Стоимость продукта",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["name", "description", "category", "price"],
            },
        ),
    ]
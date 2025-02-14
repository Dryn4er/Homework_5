from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта", null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение продукта", blank=True)
    category = models.CharField(max_length=150, verbose_name="Категория продукта")
    price = models.FloatField(verbose_name="Стоимость продукта", help_text="Введите стоимость продукта")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publication_status = models.BooleanField(default=False, blank=True, null=True, verbose_name="Статус публикации")


    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'description', 'category', 'price']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product'),
        ]


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта", null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', 'description']
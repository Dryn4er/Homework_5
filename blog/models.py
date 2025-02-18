from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое', blank=True, null=True)
    preview = models.ImageField(upload_to='blog/image', verbose_name='изображение', blank=True, null=True)
    created_at = models.DateField(verbose_name='дата создания', auto_now_add=True)
    publication_sign = models.BooleanField(verbose_name='признак публикации')
    number_of_views = models.IntegerField(verbose_name='колличество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title', 'created_at', 'number_of_views']
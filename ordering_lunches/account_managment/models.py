from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account_managment:ProductListByCategory', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Заведение")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.PositiveIntegerField(verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="обновлён")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account_managment:ProductDetail', args=[self.id, self.slug])
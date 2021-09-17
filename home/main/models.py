from django.db import models


class Carusel(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    subtitle = models.CharField('Подзаголовок', max_length=30)
    image = models.ImageField('Картинка', upload_to='static')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField('Категория', max_length=20)
    slug = models.SlugField('URL', max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

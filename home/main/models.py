from django.db import models


class Carusel(models.Model):
    title = models.CharField('Заголовок', max_length=30)
    subtitle = models.CharField('Подзаголовок', max_length=30)
    image = models.ImageField('Картинка', upload_to='static')

    def __str__(self):
        return self.title

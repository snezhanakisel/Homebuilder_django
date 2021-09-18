from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    subtitle = models.CharField('Подзаголовок', max_length=30)
    image = models.ImageField('Картинка', upload_to='static')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


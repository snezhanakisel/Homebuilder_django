from django.db import models

# Create your models here.


class Employee(models.Model):

    name = models.CharField('Имя', max_length=30)
    position = models.CharField('Должность', max_length=30)
    image = models.ImageField('Картинка', upload_to='pictures')
    description = models.CharField('Описание', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

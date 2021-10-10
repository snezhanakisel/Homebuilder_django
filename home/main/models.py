import email
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


class Mission(models.Model):
    text = models.CharField('Содержание', max_length=150)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField('Имя, профессия', max_length=20)
    email = models.EmailField('Почта')
    subject = models.CharField('Тема сообщения', max_length=30)
    message = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Feedback(models.Model):
    name = models.CharField('Имя', max_length=20)
    email = models.EmailField('Почта')
    message = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Mail(models.Model):
    """ подписка по email"""
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
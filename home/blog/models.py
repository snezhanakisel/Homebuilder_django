from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    text = models.TextField('Содержание статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    image = models.ImageField('Картинка', upload_to='blog/images')

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', verbose_name='Статья', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.CharField('Комментарий', max_length=150)
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title = 75
        if len(self.message) > len_title:
            titlestring = self.message[:len_title] + '...'
        else:
            titlestring = self.message
        return titlestring
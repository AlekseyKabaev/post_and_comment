from django.db import models

from posts.validators import title_validator

NULLABLE = {'null': True, 'blank': True}


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Введите заголовок',
                             validators=[title_validator])
    text = models.TextField(verbose_name='Текст поста')
    image = models.ImageField(upload_to="posts/", verbose_name='Изображение', **NULLABLE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.author}, {self.post}'

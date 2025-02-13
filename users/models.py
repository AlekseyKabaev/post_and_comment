from django.db import models
from django.contrib.auth.models import AbstractUser

from users.validators import password_validator, email_validator

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    login = models.CharField(max_length=50, unique=True, verbose_name='Логин', help_text='Введите логин')
    password = models.CharField(max_length=128, verbose_name='Пароль', help_text='Введите пароль',
                                validators=[password_validator])
    number = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Email', validators=[email_validator])
    birth_date = models.DateField(verbose_name='Дата рождения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login

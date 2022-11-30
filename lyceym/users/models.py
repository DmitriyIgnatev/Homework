from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserManager(UserManager):
    def active(self):
        return (
            self.get_queryset()
                .filter(is_active=True))


class CustomUser(AbstractUser):
    objects = UserManager()

    username = models.CharField(
        unique=True,
        max_length=150,
        error_messages={
            'unique': "Пользователь с таким ником уже есть"},)
    email = models.EmailField(
        'почта',
        unique=True,
        blank=False)
    password = models.CharField(
        'пароль',
        max_length=128)
    first_name = models.CharField(
        'имя',
        max_length=30,
        blank=True)
    second_name = models.CharField(
        'фамилия',
        max_length=30,
        blank=True)
    birthday = models.DateField(
        'день рождения',
        null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class OptionalCustomUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'huge user'
        verbose_name_plural = 'huge users'

    def __str__(self):
        return self.user

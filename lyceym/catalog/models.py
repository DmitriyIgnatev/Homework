from django.db import models
from .validators import Validate_amazing, validate_word, validate_number
from core.models import Core


class Item(Core):
    text = models.TextField(
        validators=[Validate_amazing('превосходно', 'куку'), ],
        verbose_name='текст')
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категории')
    tag = models.ManyToManyField('Tag', verbose_name='теги')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return f'{self.name}'


class Tag(Core):
    slug = models.SlugField(
        max_length=200,
        validators=[validate_word],
        unique=True,
        verbose_name='слэг')

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'

    def __str__(self):
        return self.name


class Category(Core):
    slug = models.SlugField(
        max_length=200,
        validators=[validate_word],
        unique=True,
        verbose_name='слэг')
    weight = models.IntegerField(
        default=100,
        validators=[validate_number],
        verbose_name='вес')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}'

from django.db import models
from .validators import Validate_amazing, validate_number
from core.models import Core
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class Item(Core):
    text = models.TextField(
        verbose_name='текст',
        validators=[Validate_amazing('превосходно', 'роскошно'), ])
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категории')
    tag = models.ManyToManyField('Tag', verbose_name='теги')
    photo = models.OneToOneField(
        'MainPhoto',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        return self.name

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo.photo,
            '300x300',
            crop='center',
            quality=51)

    def image_tmb(self):
        if self.photo:
            return mark_safe(f'<img src="{self.get_img.url}" />')
        return 'изображение не найдено'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Tag(Core):
    slug = models.SlugField(
        max_length=200,
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
        unique=True,
        verbose_name='слэг')
    weight = models.IntegerField(
        default=100,
        validators=[validate_number],
        verbose_name='вес')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категори'

    def __str__(self):
        return self.name


class MainPhoto(models.Model):
    photo = models.ImageField(
        upload_to='uploads//%Y/%m/%d/')

    class Meta:
        verbose_name = 'главная фотография'
        verbose_name_plural = 'главные фотографии'


class Gallery(models.Model):
    photo = models.ImageField(
        upload_to='uploads//%Y/%m/%d/')
    gallery = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        verbose_name='галерея')

    class Meta:
        verbose_name = 'галерея фотографии'
        verbose_name_plural = 'галерея фотографии'

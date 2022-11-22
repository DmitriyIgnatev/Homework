from django.db import models
from .validators import Validate_amazing, validate_number
from core.models import Core
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from tinymce import models as tinymce_models
from django.db.models import Prefetch


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True, category__is_published=True)
                .select_related('category')
                .order_by('category', 'name')
                .prefetch_related(
                    Prefetch('tag', queryset=Tag.objects.filter(
                        is_published=True))
                ).only('name', 'text', 'tag', 'photo', 'category__name')
        )


class Item(Core):
    objects = ItemManager()

    text = tinymce_models.HTMLField(
        verbose_name='текст',
        validators=[Validate_amazing('превосходно', 'роскошно'), ])
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категории')
    tag = models.ManyToManyField('Tag', verbose_name='теги')
    photo = models.ImageField(
        upload_to='uploads/%Y/%m/%d/',
        default='img/defaultphoto.jpg',
        verbose_name='превью')
    is_on_main = models.BooleanField(default=False, verbose_name='флаг')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
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
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    photo = models.ImageField(
        upload_to='uploads/%Y/%m/%d/', verbose_name='фото')
    gallery = models.ForeignKey(
        'Item',
        on_delete=models.CASCADE,
        verbose_name='галерея')

    class Meta:
        verbose_name = 'галерея фотографии'
        verbose_name_plural = 'галерея фотографии'

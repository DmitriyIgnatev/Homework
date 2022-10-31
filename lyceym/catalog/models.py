from django.db import models
from .validators import validate_amazing, validate_word, validate_number
from core.models import Core


class Catalog_item(Core):
    text = models.TextField(validators=[validate_amazing, ])
    category = models.ForeignKey('Catalog_category', on_delete=models.CASCADE)
    tag = models.ManyToManyField("Catalog_tag", verbose_name="Теги")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return f"{{'Имя': {self.name}, 'публикация': {self.is_published}}}"


class Catalog_tag(Core):
    slug = models.SlugField(
        max_length=200,
        validators=[validate_word],
        unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    
    def __str__(self):
        return f"имя: {self.name}, ис_паблишет: {self.is_published}"


class Catalog_category(Core):
    slug = models.SlugField(
        max_length=200,
        validators=[validate_word],
        unique=True)
    weight = models.IntegerField(default=100, validators=[validate_number])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"имя: {self.name}, ис_паблишет: {self.is_published}"

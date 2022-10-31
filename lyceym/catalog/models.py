from django.db import models
from .validators import validate_amazing, validate_word, validate_number


class Catalog_item(models.Model):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    text = models.TextField(validators=[validate_amazing, ])
    category = models.ForeignKey('Catalog_category', on_delete=models.CASCADE)
    tag = models.ManyToManyField("Catalog_tag", verbose_name="Теги")


class Catalog_tag(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(
        max_length=200,
        validators=[validate_word],
        unique=True)


class Catalog_category(models.Model):
    name = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(
        max_length=200,
        validators=[validate_word],
        unique=True)
    weight = models.IntegerField(default=100, validators=[validate_number])

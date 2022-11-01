from django.db import models


class Core(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация')
    name = models.CharField(
        max_length=150,
        verbose_name='имя')

    class Meta:
        abstract = True

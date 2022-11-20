from django.db import models


class Feedback(models.Model):
    text = models.TextField(verbose_name='текст')
    created_on = models.DateTimeField(auto_now_add=True)

from django.db import models


class FeedbackModel(models.Model):
    text = models.TextField(
        'текст',
        help_text='Поле для обратной связи',
        max_length=500)

    email = models.EmailField(
        'почта отправителя',
        help_text='эмейл')

    created_on = models.DateTimeField(
        'дата',
        help_text='Дата создания фидбека',
        auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Фидбэк'

    def __str__(self):
        return self.email

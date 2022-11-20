from django.db import models
from django import forms


class FeedbackModel(models.Model):
    text = models.CharField(
        'текст',
        help_text='Поле для обратной связи',
        max_length=500)

    created_on = models.DateTimeField(
        'дата',
        help_text='Дата создания фидбека',
        auto_now_add=True)


class Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FeedbackModel
        fields = ('text',)
        labels = {
            'text': 'текст'}
        help_text = {
            FeedbackModel.text.field.help_text: 'помогаем'}
        labels = {
            FeedbackModel.text.field.name: 'текст'}

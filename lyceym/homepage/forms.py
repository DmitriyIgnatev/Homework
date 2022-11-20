from django.db import models
from django import forms


class HomePageModel(models.Model):
    name = models.CharField(
        'Имя',
        max_length=150,
        help_text='Максимум 150 символов')

    email = models.EmailField(
        'Почта',
        max_length=150,
        help_text='Максимум 150 символов')


class Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = HomePageModel
        fields = '__all__'
        labels = {
            'name': 'имя',
            'email': 'почта'}
        help_text = {
            HomePageModel.name.field.name: 'помогаем'}
        labels = {
            HomePageModel.name.field.name: 'название'}

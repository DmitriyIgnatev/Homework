from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',
            'second_name',
            'birthday')

        widgets = {
            'birthday': MyDateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'


class ProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'second_name',
            'birthday')
        labels = {
            'first_name': 'Имя',
            'second_name': 'Фамилия',
            'birthday': 'День рождения',
        }
        widgets = {
            'birthday': MyDateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

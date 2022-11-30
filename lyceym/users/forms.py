from .models import CustomUser
from django import forms


class MyDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         models = CustomUser
#         fields = (CustomUser.birthday.field.name, )
#         widget = ({
#             'birthday': forms.DateInput(attrs={'type': 'date'})})


class RegistrationForm(forms.ModelForm):
    birthday = forms.DateField(
        label='Дата рождения',
        required=True,
        widget=MyDateInput({
            'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomUser
        fields = (
            CustomUser.username.field.name,
            CustomUser.email.field.name,
            CustomUser.password.field.name,
            CustomUser.first_name.field.name,
            CustomUser.second_name.field.name,)
        widget = ({
            CustomUser.birthday.field.name: forms.DateInput(attrs={
                'type': 'date'})})


class ProfileForm(forms.Form):
    username = forms.CharField(label='имя пользователя', max_length=150)
    email = forms.EmailField(label='почта')
    first_name = forms.CharField(label='имя', max_length=150)
    second_name = forms.CharField(label='фамилия', max_length=150)
    birthday = forms.DateField(
        label='Дата рождения',
        required=True,
        widget=MyDateInput({
            'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

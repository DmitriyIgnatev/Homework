from .models import FeedbackModel
from django import forms


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FeedbackModel
        fields = ('text', 'email')
        labels = {
            'text': 'текст',
            'email': 'ваша почта'}
        help_text = {
            FeedbackModel.text.field.help_text: 'помогаем'}
        labels = {
            FeedbackModel.text.field.name: 'текст'}

from .forms import FeedbackForm
from django.test import Client, TestCase
from django.urls import reverse

from .models import FeedbackModel


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_new_label(self):
        new_label = FormTest.form.fields['text'].label
        self.assertEqual(new_label, 'текст')

    def test_new_help_text(self):
        new_help_text = FormTest.form.fields['text'].help_text
        self.assertEqual(new_help_text, 'Поле для обратной связи')

    def test_create_task(self):
        feedback_count = FeedbackModel.objects.count()
        form_data = {
            'text': 'Тест',
            'email': 'Duck123321@yandex.ru'
            }
        form = FeedbackForm(
            data=form_data)

        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True)

        self.assertRedirects(response, reverse('feedback:feedback'))
        self.assertEqual(FeedbackModel.objects.count(), feedback_count + 1)
        self.assertTrue(form.is_valid())

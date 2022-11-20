from .forms import Form
from django.test import Client, TestCase
from django.urls import reverse
from catalog.models import Item


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = Form()

    def test_new_label(self):
        new_label = FormTest.form.fields['text'].label
        self.assertEqual(new_label, 'текст')

    def test_new_help_text(self):
        new_help_text = FormTest.form.fields['text'].help_text
        self.assertEqual(new_help_text, 'Поле для обратной связи')

    def test_create_task(self):
        item_count = Item.objects.count()
        form_data = {
            'text': 'Тест'}

        response = Client().post(
            reverse('feedback:feedback'),
            data=form_data,
            follow=True)

        self.assertRedirects(response, reverse('feedback:feedback'))

        self.assertEqual(Item.objects.count(), item_count)

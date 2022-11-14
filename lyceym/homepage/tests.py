from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/home/')
        self.assertEqual(response.status_code, 404)

    def test_notfail(self):
        response = Client().get('/home/1w3')
        self.assertEqual(response.status_code, 404)

    def test_homepage(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_notfail_more(self):
        response = Client().get('/home/something')
        self.assertEqual(response.status_code, 404)


class TaskPagesTest(TestCase):
    def test_homepage_show_correct_context(self):
        responce = Client().get(reverse('homepage:homepage'))
        self.assertIn('item', responce.context)

    def test_homepageshow_correct_context(self):
        responce = Client().get(reverse('homepage:homepage'))
        self.assertEqual(len(responce.context), 5)

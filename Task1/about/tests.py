from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = Client().get('/about/123')
        self.assertEqual(response.status_code, 404)

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = Client().get('/about/1g3')
        self.assertEqual(response.status_code, 404)

    def test_about_more(self):
        response = Client().get('/about/something')
        self.assertEqual(response.status_code, 404)

    def test_about_smth(self):
        response = Client().get('/about/123123')
        self.assertEqual(response.status_code, 404)

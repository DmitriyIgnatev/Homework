from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_fail(self):
        response = Client().get('/home/123')
        self.assertEqual(response.status_code, 200)  # Провальный тест
    
    def test_notfail(self):
        response = Client().get('/home/123')
        self.assertEqual(response.status_code, 404)
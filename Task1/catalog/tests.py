from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/12')
        self.assertEqual(response.status_code, 200)

    def test_not_exist(self):
        response = Client().get('/catalog/fghgf')
        self.assertEqual(response.status_code, 404)

    def test_catalog_mixed_vallue(self):
        response = Client().get('/catalog/12dfg')
        self.assertEqual(response.status_code, 200)

    def test_exist(self):
        response = Client().get('/catalog/fail')
        self.assertEqual(response.status_code, 200)  # Это провальный тест

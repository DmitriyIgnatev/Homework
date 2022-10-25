from django.test import Client, TestCase


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

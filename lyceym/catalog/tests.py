from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/12/')
        self.assertEqual(response.status_code, 200)

    def test_str_endpoint(self):
        response = Client().get('/catalog/fghgf/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_mixed_vallue_endpoint(self):
        response = Client().get('/catalog/12dfg/')
        self.assertEqual(response.status_code, 404)

    def test_not_normal_number_endpoint(self):
        response = Client().get('/catalog/1ggg/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_endpoint_more(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_new_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_minus_endpoint(self):
        response = Client().get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_numandcup_endpoint(self):
        response = Client().get('/catalog/-1something/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_zero_endpoint(self):
        response = Client().get('/catalog/0something/')
        self.assertEqual(response.status_code, 404)

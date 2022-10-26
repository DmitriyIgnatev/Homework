from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/12/')
        self.assertEqual(response.status_code, 200)

    def test_str_endpoint(self):
        response = Client().get('/catalog/fghgf')
        self.assertEqual(response.status_code, 404)

    def test_catalog_mixed_vallue_endpoint(self):
        response = Client().get('/catalog/12dfg')
        self.assertEqual(response.status_code, 404)

    def test_not_normal_number_endpoint(self):
        response = Client().get('/catalog/1ggg')
        self.assertEqual(response.status_code, 404)

    def test_catalog_endpoint_more(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_new_test_1_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_2_endpoint(self):
        response = Client().get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_3_endpoint(self):
        response = Client().get('/catalog/-1smth/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_4_endpoint(self):
        response = Client().get('/catalog/0d/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_5_endpoint(self):
        response = Client().get('/catalog/smth0/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_6_endpoint(self):
        response = Client().get('/catalog/smth-1/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_7_endpoint(self):
        response = Client().get('/catalog/1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_8_endpoint(self):
        response = Client().get('/catalog/1.2smth/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_9_endpoint(self):
        response = Client().get('/catalog/smth1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_10_endpoint(self):
        response = Client().get('/catalog/-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_11_endpoint(self):
        response = Client().get('/catalog/smth-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_12_endpoint(self):
        response = Client().get('/catalog/-1.2smth/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_13_endpoint(self):
        response = Client().get('/catalog/12/2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_14_endpoint(self):
        response = Client().get('/catalog/12smth12/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_15_endpoint(self):
        response = Client().get('/catalog/-12smth-12/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_16_endpoint(self):
        response = Client().get('/catalog/-1.2smth-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_17_endpoint(self):
        response = Client().get('/catalog/1.2smth1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_18_endpoint(self):
        response = Client().get('/catalog/1.2smth-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_19_endpoint(self):
        response = Client().get('/catalog/-123smth124/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_20_endpoint(self):
        response = Client().get('/catalog/-1.2smth1234/')
        self.assertEqual(response.status_code, 404)

    def test_new_test_21_endpoint(self):
        response = Client().get('/catalog/-123smth1234/')
        self.assertEqual(response.status_code, 404)

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
        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)

    def test_new_test_2_endpoint(self):
        response = Client().get('/catalog/-1')
        self.assertEqual(response.status_code, 404)

    def test_new_test_3_endpoint(self):
        response = Client().get('/catalog/-1smth')
        self.assertEqual(response.status_code, 404)

    def test_new_test_4_endpoint(self):
        response = Client().get('/catalog/0d')
        self.assertEqual(response.status_code, 404)

    def test_new_test_5_endpoint(self):
        response = Client().get('/catalog/smth0')
        self.assertEqual(response.status_code, 404)

    def test_new_test_6(self):
        response = Client().get('/catalog/smth-1')
        self.assertEqual(response.status_code, 404)

    def test_new_test_7(self):
        response = Client().get('/catalog/1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_8(self):
        response = Client().get('/catalog/1.2smth')
        self.assertEqual(response.status_code, 404)

    def test_new_test_9(self):
        response = Client().get('/catalog/smth1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_10(self):
        response = Client().get('/catalog/-1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_11(self):
        response = Client().get('/catalog/smth-1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_12(self):
        response = Client().get('/catalog/-1.2smth')
        self.assertEqual(response.status_code, 404)

    def test_new_test_13(self):
        response = Client().get('/catalog/12/2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_14(self):
        response = Client().get('/catalog/12smth12')
        self.assertEqual(response.status_code, 404)

    def test_new_test_15(self):
        response = Client().get('/catalog/-12smth-12')
        self.assertEqual(response.status_code, 404)

    def test_new_test_16(self):
        response = Client().get('/catalog/-1.2smth-1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_17(self):
        response = Client().get('/catalog/1.2smth1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_18(self):
        response = Client().get('/catalog/1.2smth-1.2')
        self.assertEqual(response.status_code, 404)

    def test_new_test_19(self):
        response = Client().get('/catalog/-123smth124')
        self.assertEqual(response.status_code, 404)

    def test_new_test_20(self):
        response = Client().get('/catalog/-1.2smth1234')
        self.assertEqual(response.status_code, 404)

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

    def test_catalog_new_test_endpoint(self):
        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tewrst_endpoint(self):
        response = Client().get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_teast_endpoint(self):
        response = Client().get('/catalog/-1smth/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_teahst_endpoint(self):
        response = Client().get('/catalog/0d/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tegst_endpoint(self):
        response = Client().get('/catalog/smth0/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tedst_endpoint(self):
        response = Client().get('/catalog/smth-1/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tesjt_endpoint(self):
        response = Client().get('/catalog/1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_testc_endpoint(self):
        response = Client().get('/catalog/1.2smth/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tesst_endpoint(self):
        response = Client().get('/catalog/smth1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tesgt_endpoint(self):
        response = Client().get('/catalog/smth-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tehsst_endpoint(self):
        response = Client().get('/catalog/-1.2smth/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tedfst_endpoint(self):
        response = Client().get('/catalog/12/2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_teaskt_endpoint(self):
        response = Client().get('/catalog/12smth12/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tedhst_endpoint(self):
        response = Client().get('/catalog/-12smth-12/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tejst_endpoint(self):
        response = Client().get('/catalog/-1.2smth-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tesgst_endpoint(self):
        response = Client().get('/catalog/1.2smth1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_teshst_endpoint(self):
        response = Client().get('/catalog/1.2smth-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_tesqwt_endpoint(self):
        response = Client().get('/catalog/-123smth124/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_teerst_endpoint(self):
        response = Client().get('/catalog/-1.2smth1234/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_teqst_endpoint(self):
        response = Client().get('/catalog/-123smth1234/')
        self.assertEqual(response.status_code, 404)

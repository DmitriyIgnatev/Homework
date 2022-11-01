from django.test import Client, TestCase
from .models import Item, Tag, Category
from django.core.exceptions import ValidationError


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/12/')
        self.assertEqual(response.status_code, 200)

    def test_minus_endpoint(self):
        response = Client().get('/catalog/-5/')
        self.assertEqual(response.status_code, 404)

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

    def test_catalog_new_numandcup_endpoint(self):
        response = Client().get('/catalog/-1something/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_zero_endpoint(self):
        response = Client().get('/catalog/0something/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_number_endpoint(self):
        response = Client().get('/catalog/something-124/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_nor_endpoint(self):
        response = Client().get('/catalog/1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_nr_endpoint(self):
        response = Client().get('/catalog/-1.2/')
        self.assertEqual(response.status_code, 404)

    def test_catalog_new_r_endpoint(self):
        response = Client().get('/catalog/-1.2ggg/')
        self.assertEqual(response.status_code, 404)


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тест',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Test',
            slug='tag-category-test')

    def test_able_create_one_item(self):
        item_count = Item.objects.count()
        self.item = Item(
            name='catalog', category=self.category,
            text='test tex роскошно')
        self.item.full_clean()
        self.item.save()
        self.item.tag.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count + 1)


class ModelsTestTwo(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Another_test',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Another_test',
            slug='tag-category-test')

    def test_unable_create_one_item(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name='catalog',
                category=self.category,
                text='test text')
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Item.objects.count(), item_count)


class ModelsTestThree(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тест',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Test',
            slug='tag-category-test')

    def test_unable_create_one_category(self):
        item_count = Category.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Category(
                name='category',
                slug='slug Error',
                weight=10000)
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Category.objects.count(), item_count)


class ModelsTestFour(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тест',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Test',
            slug='tag-category-test')

    def test_able_create_one_category(self):
        item_count = Category.objects.count()
        self.item = Category(
            name='category',
            slug='some-slug',
            weight=10000)
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Category.objects.count(), item_count + 1)


class ModelsTestFive(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тест',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Test',
            slug='tag-category-test')

    def test_unable_create_tag(self):
        item_count = Tag.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Tag(
                name='молоко',
                slug='slug Error')
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Tag.objects.count(), item_count)

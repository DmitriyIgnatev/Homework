from django.test import Client, TestCase
from .models import Item, Tag, Category
from django.core.exceptions import ValidationError
from django.urls import reverse


class StaticURLTests(TestCase):

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
            name='Молочные продукты',
            slug='Milk')

        cls.tag = Tag.objects.create(
            name='Молоко',
            slug='MilksProdukt')

    def test_able_create_one_item(self):
        item_count = Item.objects.count()
        category = Category.objects.create(
            name='Тестовая категория',
            slug='slug',
            weight=16)
        self.item = Item(
            name='catalog',
            category=category,
            text='test tex роскошно',
            id=6)
        self.item.full_clean()
        self.item.save()
        self.item.tag.add(self.tag)
        self.assertEqual(Item.objects.count(), item_count + 1)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()


class ModelsTestThree(TestCase):
    @classmethod
    def setUpClassThree(cls):
        super().setUpClassThree()
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
                weight=10000,
                id=3)
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Category.objects.count(), item_count)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()


class ModelsTestFour(TestCase):
    @classmethod
    def setUpClassFour(cls):
        super().setUpClassFour()
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
            weight=10000,
            id=2)
        self.item.full_clean()
        self.item.save()
        self.assertEqual(Category.objects.count(), item_count + 1)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()


class ModelsTestTwo(TestCase):
    @classmethod
    def setUpClassTwo(cls):
        super().setUpClassTwo()
        cls.category = Category.objects.create(
            name='Another_test',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Another_test',
            slug='tag-category-test')

    def test_unable_create_one_item(self):
        item_count = Item.objects.count()
        category = Category.objects.create(
            name='Тестовая категория',
            slug='slug',
            weight=16)
        with self.assertRaises(ValidationError):
            self.item = Item(
                name='catalog',
                category=category,
                text='test text',
                id=4)
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Item.objects.count(), item_count)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()


class ModelsTestFive(TestCase):
    @classmethod
    def setUpClassFive(cls):
        super().setUpClassFive()
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
                slug='slug Error',
                id=1)
            self.item.full_clean()
            self.item.save()
        self.assertEqual(Tag.objects.count(), item_count)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()


class TaskCatalogTest(TestCase):
    def test_catalog_request(self):
        responce = Client().get(reverse('catalog:catalog'))
        self.assertIn('items', responce.context)

    def test_catalog_correct_context(self):
        responce = Client().get(reverse('catalog:catalog'))
        self.assertEqual(len(responce.context), 5)


class ModelsTestContext(TestCase):
    @classmethod
    def setUpClassContext(cls):
        super().setUpClassFive()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Тестовый тэг',
            slug='tag-category-test')

    def test_unable_create_tag(self):
        category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-test')

        self.item = Item(
                name='молоко',
                text='Просто тест превосходно',
                category=category,
                )
        self.item.full_clean()
        self.item.save()
        response = Client().get(reverse('catalog:catalog'))
        self.assertEqual(response.context['items'].get(), self.item)
        self.assertEqual(len(response.context), 5)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()

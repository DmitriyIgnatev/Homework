from django.test import Client, TestCase
from django.urls import reverse
from catalog.models import Category, Item, Tag


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


class TaskPagesTest(TestCase):
    def test_homepage_request(self):
        responce = Client().get(reverse('homepage:homepage'))
        self.assertIn('items', responce.context)

    def test_homepage_show_correct_context(self):
        responce = Client().get(reverse('homepage:homepage'))
        self.assertEqual(len(responce.context), 5)


# Проверка на то, что на хомпейдж есть обьект при is_on_main=False
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
                name='homepage',
                text='Просто тест превосходно',
                category=category,
                is_on_main=True) 
        self.item.full_clean()
        self.item.save()
        response = Client().get(reverse('homepage:homepage'))
        self.assertEqual(response.context['items'].get(), self.item)
        self.assertEqual(len(response.context), 5)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()


# Проверка на то, что на хомпейдж нет обьектов при is_on_main=False
class ModelsTestaHomePAgeContext(TestCase):
    @classmethod
    def setUpClassContext(cls):
        super().setUpClassFive()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-test')

        cls.tag = Tag.objects.create(
            name='Тестовый тэг',
            slug='tag-category-test')

    def tes_main_published(self):
        category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-test')

        self.item = Item(
                name='homepage',
                text='Просто тест превосходно',
                category=category,
                is_on_main=False)  
        self.item.full_clean()
        self.item.save()
        response = Client().get(reverse('homepage:homepage'))
        self.assertEqual(response.context.get, [])
        self.assertEqual(len(response.context), 5)

    def tearDown(self):
        super().tearDown()
        Category.objects.all().delete()
        Item.objects.all().delete()
        Tag.objects.all().delete()

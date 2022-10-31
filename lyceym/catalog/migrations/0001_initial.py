# Generated by Django 4.1.2 on 2022-10-31 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='catalog_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200)),
                ('weight', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Catalog_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('is_published', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
    ]

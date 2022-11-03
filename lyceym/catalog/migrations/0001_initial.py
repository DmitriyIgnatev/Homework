# Generated by Django 3.2 on 2022-11-03 06:47

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='слэг')),
                ('weight', models.IntegerField(default=100, validators=[catalog.validators.validate_number], verbose_name='вес')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='слэг')),
            ],
            options={
                'verbose_name': 'тэг',
                'verbose_name_plural': 'тэги',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='публикация')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('text', models.TextField(validators=[catalog.validators.Validate_amazing('превосходно', 'роскошно')], verbose_name='текст')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категории')),
                ('tag', models.ManyToManyField(to='catalog.Tag', verbose_name='теги')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]

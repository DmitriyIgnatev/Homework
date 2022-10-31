# Generated by Django 4.1.2 on 2022-10-31 08:20

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog_item',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.catalog_category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog_item',
            name='tag',
            field=models.ManyToManyField(to='catalog.catalog_tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='catalog_category',
            name='slug',
            field=models.SlugField(max_length=200, validators=[catalog.validators.validate_word]),
        ),
        migrations.AlterField(
            model_name='catalog_category',
            name='weight',
            field=models.IntegerField(default=100, validators=[catalog.validators.validate_number]),
        ),
        migrations.AlterField(
            model_name='catalog_item',
            name='text',
            field=models.TextField(validators=[catalog.validators.validate_amazing]),
        ),
        migrations.AlterField(
            model_name='catalog_tag',
            name='slug',
            field=models.SlugField(max_length=200, validators=[catalog.validators.validate_word]),
        ),
    ]

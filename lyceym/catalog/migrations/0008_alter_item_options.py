# Generated by Django 4.1.3 on 2022-11-13 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_item_is_on_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]

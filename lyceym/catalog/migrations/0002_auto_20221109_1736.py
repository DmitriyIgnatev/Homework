# Generated by Django 3.2 on 2022-11-09 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='uploads//%Y/%m/%d/'),
        ),
        migrations.DeleteModel(
            name='MainPhoto',
        ),
    ]
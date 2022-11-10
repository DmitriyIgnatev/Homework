# Generated by Django 3.2 on 2022-11-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_item_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(upload_to='uploads//%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='img/defaultphoto.jpg', upload_to='uploads/%Y/%m/%d/', verbose_name='превью'),
        ),
    ]
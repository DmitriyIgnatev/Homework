# Generated by Django 3.2.4 on 2022-11-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Поле для обратной связи', max_length=500, verbose_name='текст')),
                ('email', models.EmailField(help_text='эмейл', max_length=254, verbose_name='почта отправителя')),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text='Дата создания фидбека', verbose_name='дата')),
            ],
            options={
                'verbose_name_plural': 'Фидбэк',
            },
        ),
    ]

# Generated by Django 3.0.2 on 2022-06-28 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
    ]

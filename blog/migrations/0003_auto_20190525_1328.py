# Generated by Django 2.2.1 on 2019-05-25 13:28

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=martor.models.MartorField(),
        ),
    ]

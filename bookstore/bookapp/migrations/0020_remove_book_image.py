# Generated by Django 3.1.2 on 2022-04-12 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0019_auto_20220412_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
    ]
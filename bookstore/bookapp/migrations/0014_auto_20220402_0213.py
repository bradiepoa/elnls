# Generated by Django 3.1.2 on 2022-04-01 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0013_book_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='cover',
            new_name='image',
        ),
    ]
# Generated by Django 3.1.2 on 2022-04-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0015_auto_20220411_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]

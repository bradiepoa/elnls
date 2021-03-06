# Generated by Django 3.1.2 on 2022-04-11 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0018_auto_20220411_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

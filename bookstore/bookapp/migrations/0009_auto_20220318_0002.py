# Generated by Django 3.1.2 on 2022-03-17 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0008_auto_20220204_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(blank=True, choices=[('pdf', 'PDF'), ('hard copy', 'hard copy')], max_length=200, null=True),
        ),
    ]

# Generated by Django 3.1.2 on 2022-02-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_auto_20220204_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_date', models.DateField(editable=False)),
                ('updated', models.DateTimeField()),
            ],
        ),
    ]
# Generated by Django 3.2.8 on 2021-10-29 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211029_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='hdmi',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='memory_card',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
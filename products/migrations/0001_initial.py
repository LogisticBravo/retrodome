# Generated by Django 3.2.8 on 2021-10-28 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=254)),
                ('model_name', models.CharField(max_length=254)),
                ('alternate_names', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('launched', models.CharField(max_length=254)),
                ('console_family', models.CharField(max_length=254)),
                ('console_type', models.CharField(max_length=254)),
                ('input_method', models.CharField(max_length=254)),
                ('hard_disk', models.CharField(max_length=254)),
                ('ram', models.CharField(max_length=254)),
                ('processor', models.CharField(max_length=254)),
                ('weight', models.CharField(blank=True, max_length=254, null=True)),
                ('battery_type', models.CharField(blank=True, max_length=254, null=True)),
                ('screen_size', models.CharField(blank=True, max_length=254, null=True)),
                ('graphics', models.BooleanField(blank=True, default=False, null=True)),
                ('hdmi', models.BooleanField(blank=True, default=False, null=True)),
                ('usb', models.BooleanField(blank=True, default=False, null=True)),
                ('has_wifi', models.BooleanField(blank=True, default=False, null=True)),
                ('ethernet', models.BooleanField(blank=True, default=False, null=True)),
                ('memory_card', models.BooleanField(blank=True, default=False, null=True)),
                ('av_digital_output', models.BooleanField(blank=True, default=False, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]

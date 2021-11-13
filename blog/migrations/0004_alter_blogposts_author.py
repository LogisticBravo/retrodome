# Generated by Django 3.2.8 on 2021-11-13 20:58

from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20211104_1530'),
        ('blog', '0003_alter_blogposts_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='author',
            field=models.ForeignKey(default=profiles.models.UserProfile, on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile'),
        ),
    ]

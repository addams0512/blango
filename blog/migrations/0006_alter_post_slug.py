# Generated by Django 3.2.6 on 2023-11-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_authorprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

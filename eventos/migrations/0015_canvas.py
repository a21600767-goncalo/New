# Generated by Django 3.2.3 on 2021-09-04 14:52

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0014_auto_20210821_0058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canvas', cloudinary.models.CloudinaryField(max_length=255, verbose_name='canvas')),
            ],
        ),
    ]

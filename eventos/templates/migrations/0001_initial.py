# Generated by Django 3.1.6 on 2021-04-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id_imagem', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]

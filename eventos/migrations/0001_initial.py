# Generated by Django 3.2.3 on 2021-06-20 23:51

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id_evento', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistas', models.CharField(default='', max_length=64)),
                ('titulo_evento', models.CharField(default='', max_length=64)),
                ('descricao_evento', models.CharField(default='', max_length=500)),
                ('data_evento', models.DateField(blank=True, default=datetime.datetime.now)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id_noticia', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_noticia', models.CharField(max_length=30)),
                ('descricao_noticia', models.CharField(max_length=64)),
                ('data_noticia', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id_video', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id_projeto', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_projeto', models.CharField(default='', max_length=35)),
                ('descricao_projeto', models.CharField(default='', max_length=500)),
                ('duracao_projeto', models.IntegerField(default=0)),
                ('data_projeto', models.DateField(blank=True, default=datetime.datetime.now)),
                ('video_projeto', models.ManyToManyField(to='eventos.Videos')),
            ],
        ),
        migrations.CreateModel(
            name='Evento2',
            fields=[
                ('id_evento', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistas', models.CharField(default='', max_length=64)),
                ('titulo_evento', models.CharField(default='', max_length=64)),
                ('descricao_evento', models.CharField(default='', max_length=500)),
                ('data_evento', models.DateField(blank=True, default=datetime.datetime.now)),
                ('imagens_evento', models.ManyToManyField(to='eventos.Imagens')),
            ],
        ),
    ]
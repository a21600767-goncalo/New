# Generated by Django 3.2.3 on 2021-06-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_auto_20210629_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento2',
            name='projeto',
        ),
        migrations.AddField(
            model_name='projeto',
            name='evento',
            field=models.ManyToManyField(to='eventos.Evento2'),
        ),
    ]
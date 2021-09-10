# Generated by Django 3.2.3 on 2021-09-09 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0018_auto_20210904_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='artistas',
            new_name='autores',
        ),
        migrations.AddField(
            model_name='evento2',
            name='artistas',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='evento2',
            name='local',
            field=models.CharField(default='', max_length=500),
        ),
    ]

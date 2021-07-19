# Generated by Django 3.2.3 on 2021-06-21 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20210621_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento2',
            name='imagens',
        ),
        migrations.AddField(
            model_name='evento2',
            name='images',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='imagens',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.evento2'),
        ),
    ]
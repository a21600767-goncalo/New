from django.db import models



class Imagens(models.Model):
    id_imagem=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    imagens=models.ImageField(default='')
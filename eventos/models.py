from django.db import models
from datetime import datetime
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.shortcuts import render, redirect, get_object_or_404


# Create your models here.




class Videos(models.Model):
    id_video=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    videos= models.URLField(default='')

    def __str__(self):
        return f"{self.id_video} {self.videos}"

class Projeto(models.Model):
    id_projeto=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo_projeto= models.CharField(max_length=64, default='')
    artistas = models.CharField(max_length=64, default="")
    programa= models.TextField(max_length=1000, default='')
    notas = models.CharField(max_length=64, default='')

    def get_absolute_url(self):
        return reverse('projetos', kwargs={'pk': self.id_projeto})

    def get_absolute_url_eventos(self):
        return reverse('eventos', kwargs={'pk': self.id_evento})

    def __str__(self):
        return f"{self.titulo_projeto}"

class Evento2(models.Model):
    id_evento =models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo_evento = models.CharField(max_length=64, default="")
    descricao_evento = models.CharField(max_length=500, default="")
    data_evento = models.DateField(default=datetime.now, blank=True)
    projeto =models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)
    video_evento=models.ManyToManyField(Videos, blank=True)

    def __str__(self):
        return f"{self.titulo_evento}"

    def get_absolute_url(self):
        return reverse('eventos', kwargs={'pk': self.id_evento, 'pk2': self.data_evento})

    @property
    def agrega(self):
        return ' '.join(imagens.images for Imagens in self.images_set.all())

        
    
class Imagens(models.Model):
    evento = models.ForeignKey(Evento2, on_delete=models.CASCADE, null=True)
    images = CloudinaryField('images')
    

    



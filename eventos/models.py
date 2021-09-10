from django.db import models
from datetime import datetime
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.shortcuts import render, redirect, get_object_or_404


# Create your models here.

class agendamento(models.Model):
    promocao= models.DateTimeField(default=datetime.now, blank=True)

    
    def __str__(self):
        return f"{self.promocao}"

class Videos(models.Model):
    id_video=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    videos= models.URLField(default='')

    def __str__(self):
        return f"{self.id_video} {self.videos}"

class Projeto(models.Model):
    id_projeto=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo_projeto= models.CharField(max_length=200, default='')
    autores = models.CharField(max_length=200, default="")
    programa= models.TextField(max_length=20000, default='')
    notas = models.CharField(max_length=200, default='')

    def get_absolute_url(self):
        return reverse('projetos', kwargs={'pk': self.id_projeto})


    def __str__(self):
        return f"{self.titulo_projeto}"

class Evento2(models.Model):
    id_evento =models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titulo_evento = models.CharField(max_length=200, default="")
    descricao_evento = models.TextField(max_length=20000, default="")
    data_evento = models.DateField(default=datetime.now, blank=True)
    local=models.CharField(max_length=200, default="")
    artistas = models.CharField(max_length=200, default="")
    projeto =models.ForeignKey(Projeto, on_delete=models.CASCADE, null=True)
    video_evento=models.ManyToManyField(Videos, blank=True)
    data_promocao = models.ForeignKey(agendamento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.titulo_evento} {self.data_promocao}"

    def get_absolute_url(self):
        return reverse('eventos', kwargs={'pk': self.id_evento, 'pk2': self.data_evento})


class Canvas(models.Model):
    id_canvas =models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    def __str__(self):
        return f"{self.id_canvas}"

class ImagensCanvas(models.Model):
    canvasFK = models.ForeignKey(Canvas, on_delete=models.CASCADE, null=True)
    canvas = CloudinaryField('canvas')

    def __str__(self):
        return f"{self.canvas}"
        
    
class Imagens(models.Model):
    evento = models.ForeignKey(Evento2, on_delete=models.CASCADE, null=True)
    images = CloudinaryField('images')
    

## teste commit
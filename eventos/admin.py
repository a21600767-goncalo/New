from django.contrib import admin

from .models import  Projeto, Videos, Evento2, Imagens, agendamento, Canvas, ImagensCanvas
# Register your models here.

class agendamentoAdmin(admin.StackedInline):
    model = agendamento

class ImagensCanvasAdmin(admin.StackedInline):
    model = ImagensCanvas

class ImagensAdmin(admin.StackedInline):
    model = Imagens

class EventInline(admin.StackedInline):
    model = Evento2


class ProjetoAdmin(admin.ModelAdmin):
    list_display =("id_projeto", "titulo_projeto", "autores")
    search_fields=("id_projeto", "titulo_projeto", "descricao_projeto")
    
    

class Evento2Admin(admin.ModelAdmin):
    list_display =("titulo_evento", "data_evento")
    
    inlines = [ImagensAdmin,]

class VideosAdmin(admin.ModelAdmin):
    list_display=("id_video", "videos")

    
class CanvasAdmin(admin.ModelAdmin):
    
    inlines = [ImagensCanvasAdmin,]

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Imagens)
admin.site.register(agendamento)
admin.site.register(Evento2, Evento2Admin)
admin.site.register(Canvas, CanvasAdmin)


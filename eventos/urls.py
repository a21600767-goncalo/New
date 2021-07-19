from django.urls import path, include
from django.contrib import admin



from . import views


urlpatterns = [

    path("", views.index),
    
   
    path("index/home", views.home, name='home'),
    path("index/membros",views.Membros, name='membros'),
    path("index/colaboracao",views.colaboracao, name='colaboracao'),
    path("index/historia",views.Historia, name='historia'),
    path("index/livrohonra",views.LivroHonra, name='livrohonra'),
    path("eventos_new/", views.Eventos_new, name="eventos_new"),
    path("quem_somos_new", views.Quem_somos_new, name="quem_somos_new"),
    path("projetos", views.projetos, name="projetos"),
    path('projetos/<int:id>/', views.detail_view_projetos, name="projeto"),


    path("registo/", views.UserRegisterView2, name= "registo"),
    path("login/", views.loginPage, name= "login"),
    path("logout/", views.loginPage, name= "logout"),
    
    path('eventos/<id>/<data>/', views.detail_view_eventos, name='eventos'),
    
]

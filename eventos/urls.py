from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("home", views.home, name='home'),
    path("", views.home, name='home'),
    path("membros",views.Membros, name='membros'),
    path("historia",views.Historia, name='historia'),
    path("index/livrohonra",views.LivroHonra, name='livrohonra'),
    path("eventos_new/", views.Eventos_new, name="eventos_new"),
    path("quem_somos_new", views.Quem_somos_new, name="quem_somos_new"),
    path("Projetos/", views.projetos, name="Projetos"),
    path('projetos/<id>/', views.detail_view_projetos, name="projetos"),
    path('eventos/<id>/<data>/', views.detail_view_eventos, name='eventos'),
    path("registo/", views.UserRegisterView2, name="registo"),
    path("login/", views.loginPage, name="login"),
    path("canvas/<id>/<data>/", views.detail_view_canvas, name= "canvas"),
]

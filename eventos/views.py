from django.shortcuts import render, redirect, get_object_or_404
from eventos.models import Evento2, Projeto, Imagens
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def Membros(request):
    return render(request, 'Membros.html')

def colaboracao(request):
    return render(request, 'Colaboração.html')

def Historia(request):
    return render(request, 'Historia.html')

def LivroHonra(request):
    return render(request, 'Livro-De-Honra.html')

def Historia_new(request):
    return render(request, 'Historia_new.html')


def Eventos_new(request):
    eventos = Evento2.objects.all()
    projetos = Projeto.objects.all()
    date_min_eventos = request.GET.get('date_min_eventos')
    date_max_eventos = request.GET.get('date_max_eventos')
    date_min_projetos = request.GET.get('date_min_projetos')
    date_max_projetos = request.GET.get('date_max_projetos')

    ctx = {}
    xpto={}
    url_parameter = request.GET.get("a")
    if date_min_eventos != '' and date_min_eventos is not None:
        eventos = eventos.filter(data_evento__gte=date_min_eventos)
    if date_min_projetos != '' and date_min_projetos is not None: 
        projetos = projetos.filter(data_projeto__gte=date_min_projetos)
        

    if date_max_eventos != '' and date_max_eventos is not None:
        eventos = eventos.filter(data_evento__lt=date_max_eventos)
    if date_max_projetos != '' and date_max_projetos is not None:
        projetos = projetos.filter(data_projeto__lt=date_max_projetos)
        
    
   
        


    if url_parameter:   

            eventos = Evento2.objects.filter(Q(titulo_evento__icontains=url_parameter) | Q(descricao_evento__icontains=url_parameter))
            projetos = Projeto.objects.filter(Q(titulo_projeto__icontains=url_parameter) | Q(programa__icontains=url_parameter) | Q(notas__icontains=url_parameter))
    


    ctx={"eventos":eventos, "projetos":projetos}
    if request.is_ajax():

        html = render_to_string(
            template_name="eventos.html", context={"eventos":eventos, "projetos":projetos}
            )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)
    ctx={"eventos":eventos, "projetos":projetos}
    return render(request, "Eventos_new.html", context=ctx)



def Quem_somos_new(request):
    return render(request, 'Quem_somos_new.html')



def detail_view_eventos(request,id, data):
    evento= get_object_or_404(Evento2, id_evento=id, data_evento=data)
    imagens = Imagens.objects.filter(evento = evento)
    eventos = Evento2.objects.filter(id_evento= id, data_evento=data)
    return render(request, 'Pagina_evento.html', {'evento': evento, 'imagens': imagens, 'eventos': eventos})

def projetos(request):
    eventos = Evento2.objects.all()
    projetos = Projeto.objects.all()
    date_min_eventos = request.GET.get('date_min_eventos')
    date_max_eventos = request.GET.get('date_max_eventos')
    date_min_projetos = request.GET.get('date_min_projetos')
    date_max_projetos = request.GET.get('date_max_projetos')

    ctx = {}
    xpto={}
    url_parameter = request.GET.get("a")
    if date_min_eventos != '' and date_min_eventos is not None:
        eventos = eventos.filter(data_evento__gte=date_min_eventos)
    if date_min_projetos != '' and date_min_projetos is not None: 
        projetos = projetos.filter(data_projeto__gte=date_min_projetos)
        

    if date_max_eventos != '' and date_max_eventos is not None:
        eventos = eventos.filter(data_evento__lt=date_max_eventos)
    if date_max_projetos != '' and date_max_projetos is not None:
        projetos = projetos.filter(data_projeto__lt=date_max_projetos)
        
    
   
        


    if url_parameter:   

            eventos = Evento2.objects.filter(Q(titulo_evento__icontains=url_parameter) | Q(descricao_evento__icontains=url_parameter))
            projetos = Projeto.objects.filter(Q(titulo_projeto__icontains=url_parameter) | Q(programa__icontains=url_parameter) | Q(notas__icontains=url_parameter))
    


    ctx={"eventos":eventos, "projetos":projetos}
    if request.is_ajax():

        html = render_to_string(
            template_name="prj.hmtl", context={"eventos":eventos, "projetos":projetos}
            )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)
    ctx={"eventos":eventos, "projetos":projetos}
    return render(request, "Projetos.html", context=ctx)

def detail_view_projetos(request, id):
    projeto= get_object_or_404(Projeto, id_projeto=id)
    projetos = Projeto.objects.filter(id_projeto = id)
    return render(request, 'Pagina_projeto.html', {'projeto': projeto, 'projetos': projetos})



def facebook(request):
    return render(request, 'facebook-html.html')


@unauthenticated_user
def UserRegisterView2(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Utilizador criado para '+ user)
            return redirect('login')


    context = {'form' : form}
    return render(request, 'registo.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request,'Username OU Password incorreta ')

    context = {}
    return render(request, 'login.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detail_view_canvas(request,id, data):
    evento= get_object_or_404(Evento2, id_evento=id, data_evento=data)
    eventos = Evento2.objects.filter(id_evento= id, data_evento=data)
    return render(request, 'Canvas.html', {'evento': evento, 'eventos': eventos})





def logOutUser(request):
    logout(request)
    return redirect('login')    


@allowed_users(allowed_roles=['admin'])
def admin(request):
    return redirect('admin')
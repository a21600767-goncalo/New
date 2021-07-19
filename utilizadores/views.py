from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
# Create your views here.


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

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            return redirect('home') ##colocar a pagina para dar redirect
        else:
            messages.info(request,'Username OU Password incorreta ')

    context = {}
    return render(request, 'login.html', context)

def logOutUser(request):
    logout(request)
    return redirect('login')

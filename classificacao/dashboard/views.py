from django.contrib.auth import logout
from django.contrib import messages
from django.contrib import auth as django_auth
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def autenticar(request, username, senha):
    u"""."""
    usuario = django_auth.authenticate(username=username, password=senha)
    if usuario is not None:
        if usuario.is_active:
            django_auth.login(request, usuario)
    return usuario


def login_restrito(request):
    username = request.POST.get('username')
    senha = request.POST.get('password')
    usuario = autenticar(request, username, senha)
    if usuario:
        messages.success(request, 'Login realizado com sucesso!')
        return redirect('home')
    else:
        if not usuario:
            messages.error(request, 'Usuário e/ou senha incorretos.')
        else:
            messages.error(request, 'Usuário sem permissão de acesso')
            return my_logout(request, 'login_restrito')

    return render(request, 'login.html')

#     if not request.user.is_authenticated():
#         if request.method == 'POST':
#             username = "G_" + request.POST.get('username')
#             senha = request.POST.get('password')
#
#             usuario = autenticar(request, username, senha)
#
#             if usuario:
#                 messages.success(request, 'Login realizado com sucesso!')
#                 return redirect('index_restrito')
#             else:
#                 if not usuario:
#                     messages.error(request, 'Usuário e/ou senha incorretos.')
#                 else:
#                     messages.error(request, 'Usuário sem permissão de acesso')
#                 return my_logout(request, 'login_restrito')
#
#     else:
#         if request.user.is_gestor():
#             return redirect('index_restrito')
#
#     return render_to_response('geral/login_restrito.html', locals(),
#                               context_instance=RequestContext(request))


@login_required(login_url="/login/")
def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

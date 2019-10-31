from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import ClassificacaoForm


# Create your views here.
@login_required(login_url="/login/")
def classificacao(request):
    form = ClassificacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'classificacao.html', {'form': form})


@login_required(login_url="/login/")
def desclassificacao(request):
    return render(request, 'desclassificacao.html')


@login_required(login_url="/login/")
def reclassificacao(request):
    return render(request, 'reclassificacao.html')

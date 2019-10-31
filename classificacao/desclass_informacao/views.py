from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from .forms import procuraNIC, visualisar_desclass
from .models import fund_desclassificacao

@login_required(login_url="/login/")
def get_nic(request):
    form = procuraNIC(request.POST or None)
    if form.is_valid():
        # TODO precisa fatiar o NIC para salvar cada parte dele no banco
        # TODO Enviar o NIC pela url para ser carregada no form
        return redirect('desclassificacao')
    return render(request, 'procura_nic.html', {'form': form})


@login_required(login_url="/login/")
def desclassificacao(request):
        # TODO Precisa receber o NIC da pagina anterior, buscar no banco
        # TODO e popular o formulario com as informações.
    fund_desclassif = fund_desclassificacao.objects.order_by('id')

    return render(request, 'desclassificacao.html', {'fund_desclassif': fund_desclassif})
from django import forms
from django.forms import ModelForm

from class_informacao.models import classificacao


class procuraNIC(forms.Form):
    nic = forms.CharField(max_length=30)

class visualisar_desclass(ModelForm):
    # TODO precisa verificar se é preciso criar um formulário para carregar tais informações
        class Meta:
            model = classificacao
            fields = '__all__'
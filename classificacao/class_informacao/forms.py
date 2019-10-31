from django import forms
from django.forms import ModelForm

from .models import classificacao


class ClassificacaoForm (ModelForm):
    class Meta:
        model = classificacao
        exclude = ['nic']
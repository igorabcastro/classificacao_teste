from django.urls import path
from .views import  desclassificacao, get_nic


urlpatterns = [
    path('desclassificacao/', desclassificacao, name="desclassificacao"),
    path('procura_nic/', get_nic, name="procura_nic"),
]
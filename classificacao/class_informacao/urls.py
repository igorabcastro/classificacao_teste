from django.urls import path
from .views import classificacao, desclassificacao, reclassificacao


urlpatterns = [
    path('classificacao/', classificacao, name="classificacao"),
    # path('desclassificacao/', desclassificacao, name="desclassificacao"),
    path('reclassificacao/', reclassificacao, name="reclassificacao"),
]
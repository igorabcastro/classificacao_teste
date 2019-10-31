from django.db import models

# Create your models here.


class fund_desclassificacao(models.Model):
    descricao = models.CharField(max_length=250)
    def __str__(self):
        return self.descricao
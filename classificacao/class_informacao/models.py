from django.db import models

# Create your models here.
class grau_sigilo(models.Model):
    descricao = models.CharField(max_length=150)
    qnt_ano = models.IntegerField()
    cod = models.IntegerField()
    def __str__(self):
        return self.descricao


class fund_classificacao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)
    def __str__(self):
        return self.descricao


class und_gestora(models.Model):
    cod = models.IntegerField()
    sigla = models.CharField(max_length=10)
    descricao = models.CharField(max_length=150)
    def __str__(self):
        return self.descricao

class tipo_doc(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    def __str__(self):
        return self.nome


class NIC(models.Model):
    cod_und_gestora = models.ForeignKey(und_gestora, on_delete=models.CASCADE)
    id_tipo_doc = models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
    ano = models.IntegerField()
    numero = models.CharField(max_length=30)

class classificacao(models.Model):
    und_gestora = models.ForeignKey(und_gestora, on_delete=models.CASCADE)
    nic = models.ForeignKey(NIC, on_delete=models.CASCADE)
    assunto = models.TextField()
    grau_sigilo = models.ForeignKey(grau_sigilo, on_delete=models.CASCADE)
    tipo_doc = models.ForeignKey(tipo_doc, on_delete=models.CASCADE)
    data_doc = models.DateField()
    fund_classificacao = models.ForeignKey(fund_classificacao, on_delete=models.CASCADE)
    razao_calssf = models.TextField()
    data_classf_doc = models.DateField()
    autoridade_classf = models.CharField(max_length=150)
    autoridade_ratificadora = models.CharField(max_length=150)
    prazo_sigilo = models.IntegerField()
    prazo_final = models.DateField()


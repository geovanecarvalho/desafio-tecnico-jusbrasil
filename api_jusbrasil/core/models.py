from django.db import models


class Crawler(models.Model):
    numero_processo = models.CharField(unique=True, max_length=25)
    classe = models.CharField(max_length=50, blank=True, null=True)
    area = models.CharField(max_length=50, blank=True, null=True)
    assunto = models.CharField(max_length=50, blank=True, null=True)
    data_de_distribuicao = models.CharField(max_length=50, blank=True, null=True)
    juiz = models.CharField(max_length=50, blank=True, null=True)
    valor_da_acao = models.CharField(max_length=50, blank=True, null=True)
    partes_do_processo = models.TextField(blank=True, null=True)
    lista_das_movimentacao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crawler'


    def __str__(self):
        return self.numero_processo
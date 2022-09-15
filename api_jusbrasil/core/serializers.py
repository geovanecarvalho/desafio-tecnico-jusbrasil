from rest_framework import serializers
from .models import Crawler


class CrawlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crawler
        fields = ['numero_processo', 'classe', 'area', 'assunto', 'data_de_distribuicao', 'juiz', 'valor_da_acao', 'partes_do_processo', 'lista_das_movimentacao']
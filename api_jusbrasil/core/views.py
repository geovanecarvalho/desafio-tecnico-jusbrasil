from django.shortcuts import render
from rest_framework import viewsets
from .models import Crawler
from .serializers import CrawlerSerializer


class CrawlerViewSet(viewsets.ModelViewSet):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerSerializer

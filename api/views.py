from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import InvestmentGuidelineSerializer, InvestmentGuidelineOptionsSerializer, StrategySerializer
from investmentguidelines.models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy


class InvestmentGuidelineViewSet(viewsets.ModelViewSet):
    queryset = InvestmentGuideline.objects.all()
    serializer_class = InvestmentGuidelineSerializer

class InvestmentGuidelineOptionsViewSet(viewsets.ModelViewSet):
    queryset = InvestmentGuidelineOptions.objects.all()
    serializer_class = InvestmentGuidelineOptionsSerializer

class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer


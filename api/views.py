# from django.shortcuts import render

# Create your views here.
# import django_filters
# from dynamic_rest.viewsets import DynamicModelViewSet
from rest_framework import viewsets
# from rest_framework import filters


from .serializers import *
from core.models import *


class InvestmentGuidelineViewSet(viewsets.ModelViewSet):
    queryset = InvestmentGuideline.objects.all()
    serializer_class = InvestmentGuidelineSerializer

class InvestmentGuidelineOptionsViewSet(viewsets.ModelViewSet):
    queryset = InvestmentGuidelineOptions.objects.all()
    serializer_class = InvestmentGuidelineOptionsSerializer
    # filter_backends = (filters.SearchFilter,)
    # filter_fields = [
    #     'InvestmentGuideline',
    #     'strategy',
    #     'is_enhanced',
    #     'is_impact',
    # ]

class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializer

class StrategistViewSet(viewsets.ModelViewSet):
    queryset = Strategist.objects.all()
    serializer_class = StrategistSerializer

class BenchmarkViewSet(viewsets.ModelViewSet):
    queryset = Benchmark.objects.all()
    serializer_class = BenchmarkSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AssetClassViewSet(viewsets.ModelViewSet):
    queryset = AssetClass.objects.all()
    serializer_class = AssetClassSerializer
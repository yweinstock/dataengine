from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(AssetClass)
admin.site.register(Strategist)
admin.site.register(Strategy)
admin.site.register(Benchmark)
admin.site.register(Product)
admin.site.register(InvestmentCounselor)
admin.site.register(InvestmentGuideline)
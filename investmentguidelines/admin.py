from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class StrategyAdmin(admin.ModelAdmin):
    list_display = (
        'strategy_name',
        'strategist_fk',
        'asset_class',
        'benchmark_fk',
        'product_fk',
        'created_by',
        'created_date',
        'updated_by',
        'updated_date',

    )

class InvestmentGuidelineOptionsAdminInline(admin.TabularInline):
    model = InvestmentGuidelineOptions

class InvestmentGuidelineAdmin(admin.ModelAdmin):
    inlines = (InvestmentGuidelineOptionsAdminInline, )

admin.site.register(AssetClass)
admin.site.register(Strategist)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Benchmark)
admin.site.register(Product)
admin.site.register(InvestmentCounselor)
admin.site.register(InvestmentGuideline, InvestmentGuidelineAdmin)
admin.site.register(InvestmentGuidelineOptions)
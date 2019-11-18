from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
# from django.conf import settings



class Strategist(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='strategist_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='strategist_updated_by')
    def __str__(self):
        return self.last_name + ', ' + self.first_name
    class Meta:
        verbose_name = _('Strategist')
        verbose_name_plural = _('Strategists')
        ordering = ['last_name', 'first_name']


class Benchmark(models.Model):
    benchmark_name = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='benchmark_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='benchmark_updated_by')

    def __str__(self):
        return self.benchmark_name
    class Meta:
        verbose_name = _('Benchmark')
        verbose_name_plural = _('Benchmarks')
        ordering = ['benchmark_name']

class AssetClass(models.Model):
    asset_class_name = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='asset_class_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='asset_class_updated_by')

    def __str__(self):
        return self.asset_class_name
    class Meta:
        verbose_name = _('Asset Class')
        verbose_name_plural = _('Asset Classes')
        ordering = ['asset_class_name']


class Product(models.Model):
    product_name = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='product_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='product_updated_by')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['product_name']

class Strategy(models.Model):
    strategy_name = models.CharField(max_length=150, verbose_name='Strategy Name')

    strategist_fk = models.ForeignKey(Strategist, null=True, on_delete=models.CASCADE, verbose_name="Strategist")
    benchmark_fk = models.ForeignKey(Benchmark, null=True, on_delete=models.CASCADE, verbose_name="Benchmark")
    asset_class = models.ForeignKey(AssetClass, null=True, on_delete=models.CASCADE, verbose_name="Asset Class")
    product_fk = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, verbose_name="Product")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='strategy_created_by')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='strategy_updated_by')
    updated_date = models.DateTimeField(auto_now=True)

    # is_enhanced = models.BooleanField(default=False)
    # is_impact = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Strategy')
        verbose_name_plural = _('Strategies')
        ordering = ['strategy_name']


    def __str__(self):
        return self.strategy_name


class InvestmentCounselor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,related_name='investment_counselor_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,related_name='investment_counselor_updated_by')

    class Meta:
        verbose_name = _('Investment Counselor')
        verbose_name_plural = _('Investment Counselors')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class InvestmentGuideline(models.Model):
    portfolio_code = models.CharField(max_length=150, verbose_name='Portfolio Code')
    investment_counselor = models.ForeignKey(InvestmentCounselor, null=True, on_delete=models.CASCADE)
    strategies = models.ManyToManyField(Strategy,  through='InvestmentGuidelineOptions', related_name='investmentguideline')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='investment_guideline_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='investment_guideline_updated_by')
    class Meta:
        verbose_name = _('Investment Guideline')
        verbose_name_plural = _('Investment Guidelines')
        ordering = ['created_date']

    def __str__(self):
        return self.portfolio_code


class InvestmentGuidelineOptions(models.Model):
    investmentguideline = models.ForeignKey(InvestmentGuideline, on_delete=models.CASCADE, null=True, blank=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, null=True, blank=True)
    is_enhanced = models.BooleanField(default=False)
    is_impact = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='investment_guideline_options_created_by')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='investment_guideline_options_updated_by')

    class Meta:
        verbose_name = _('Investment Guideline Option')
        verbose_name_plural = _('Investment Guideline Options')
        ordering = ['investmentguideline', 'strategy']

    # def __str__(self):
    #     return self.investmentguideline.portfolio_code + ": " + self.strategy.strategy_name
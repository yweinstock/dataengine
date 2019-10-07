from django.db import models
from django.utils.translation import ugettext_lazy as _



class Strategist(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return self.last_name + ', ' + self.first_name
    class Meta:
        verbose_name = _('Strategist')
        verbose_name_plural = _('Strategists')
        ordering = ['last_name', 'first_name']


class Benchmark(models.Model):
    benchmark_name = models.CharField(max_length=300)
    def __str__(self):
        return self.benchmark_name
    class Meta:
        verbose_name = _('Benchmark')
        verbose_name_plural = _('Benchmarks')
        ordering = ['benchmark_name']

class AssetClass(models.Model):
    asset_class_name = models.CharField(max_length=300)
    def __str__(self):
        return self.asset_class_name
    class Meta:
        verbose_name = _('Asset Class')
        verbose_name_plural = _('Asset Classes')
        ordering = ['asset_class_name']


class Product(models.Model):
    product_name = models.CharField(max_length=300)
    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['product_name']

class Strategy(models.Model):
    strategy_name = models.CharField(max_length=150, verbose_name='Strategy Name')

    strategist_fk = models.ForeignKey(Strategist, null=True, on_delete=models.CASCADE)
    benchmark_fk = models.ForeignKey(Benchmark, null=True, on_delete=models.CASCADE)
    asset_class = models.ForeignKey(AssetClass, null=True, on_delete=models.CASCADE)
    product_fk = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)

    is_enhanced = models.BooleanField(default=False)
    is_impact = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Strategy')
        verbose_name_plural = _('Strategies')
        ordering = ['strategy_name']


    def __str__(self):
        return self.strategy_name


class InvestmentCounselor(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = _('Investment Counselor')
        verbose_name_plural = _('Investment Counselors')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class InvestmentGuideline(models.Model):
    portfolio_code = models.CharField(max_length=150, verbose_name='Portfolio Code')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updated_date = models.DateTimeField(auto_now_add=False, verbose_name='Updated Date')
    investment_counselor = models.ForeignKey(InvestmentCounselor, null=True, on_delete=models.CASCADE)
    strategies = models.ManyToManyField(Strategy, db_constraint=False)

    class Meta:
        verbose_name = _('Investment Guideline')
        verbose_name_plural = _('Investment Guidelines')
        ordering = ['created_date']

    def __str__(self):
        return self.portfolio_code
from django import forms
from .models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy
from django_superform import SuperModelForm, InlineFormSetField
from django.forms import modelformset_factory


class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = (
            'strategy_name',
            'strategist_fk',
            'benchmark_fk',
            'asset_class',
            'product_fk',
        )

class InvestmentGuidelineOptionsForm(forms.ModelForm):
    class Meta:
        model = InvestmentGuidelineOptions
        fields = (
            'strategy',
            'is_enhanced',
            'is_impact',
        )
#
# IGOptionsFormSet = modelformset_factory(InvestmentGuidelineOptionsForm)

class InvestmentGuidelineForm(forms.ModelForm):
    # strategies = InlineFormSetField(formset_class=IGOptionsFormSet)
    class Meta:
        model = InvestmentGuideline
        fields = (
            'portfolio_code',
            'investment_counselor',
        )
    strategies = forms.ModelMultipleChoiceField(queryset=Strategy.objects.all())
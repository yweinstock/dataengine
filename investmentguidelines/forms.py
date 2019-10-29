from django import forms
from .models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy
from django.db import transaction

from django_superform import SuperModelForm, InlineFormSetField
from django.forms import inlineformset_factory


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

IGOptionsFormSet = inlineformset_factory(
    InvestmentGuideline,
    InvestmentGuidelineOptions,
    form=InvestmentGuidelineOptionsForm,
    fields = (
        'strategy',
        'is_enhanced',
        'is_impact',
    ),
    extra=1,
    can_delete=True
)

class InvestmentGuidelineForm(forms.ModelForm):
    class Meta:
        model = InvestmentGuideline
        fields = (
            'portfolio_code',
            'investment_counselor',
        )
        label = {
            'portfolio_code': 'Portfolio Code'
        }
    # strategies = InlineFormSetField(formset_class=IGOptionsFormSet)
    # strategies = forms.ModelMultipleChoiceField(queryset=Strategy.objects.all())


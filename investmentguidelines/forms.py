from django import forms
from .models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy
from .custom_layout_object import LayoutObject, Formset
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
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
    extra=4,
    can_delete=True
)

class InvestmentGuidelineForm(forms.ModelForm):
    class Meta:
        model = InvestmentGuideline
        fields=[
            'portfolio_code',
            'investment_counselor',
        ]

    def __init__(self, *args, **kwargs):
        super(InvestmentGuidelineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.form_tag = True
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-md-3 create-label'
        # self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('portfolio_code'),
                Field('investment_counselor'),
                Fieldset('Add Strategies', Formset('investment_guideline_options')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
    # strategies = InlineFormSetField(formset_class=IGOptionsFormSet)
    # strategies = forms.ModelMultipleChoiceField(queryset=Strategy.objects.all())


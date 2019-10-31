from rest_framework import serializers
from investmentguidelines.models import InvestmentGuideline, InvestmentGuidelineOptions, Strategy

class StrategySerializer(serializers.ModelSerializer):
    strategy_name = serializers.StringRelatedField(many=False)
    class Meta:
        model = Strategy
        fields = (
            'strategy_name',
            'strategist_fk',
        )

class InvestmentGuidelineOptionsSerializer(serializers.ModelSerializer):
    strategy = StrategySerializer(many=False, read_only=True)
    class Meta:
        model = InvestmentGuidelineOptions
        fields = (
            'strategy',
            'is_enhanced',
            'is_impact',
        )


class InvestmentGuidelineSerializer(serializers.ModelSerializer):
    investment_counselor = serializers.StringRelatedField(many=False)
    strategies = InvestmentGuidelineOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = InvestmentGuideline
        fields = (
            'portfolio_code',
            'investment_counselor',
            'strategies',
            'created_date',
            'created_by',
            'updated_date',
            'updated_by',
        )


#
# class StrategySerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField(source='group.id')
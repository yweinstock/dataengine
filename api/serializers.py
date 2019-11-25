from rest_framework import serializers
# from dynamic_rest.serializers import DynamicModelSerializer, DynamicRelationField
# from dynamic_rest.serializers import DynamicModelSerializer
from core.models import *

class StrategySerializer(serializers.ModelSerializer):
    strategy_name = serializers.StringRelatedField(many=False)
    strategist_fk = serializers.StringRelatedField(many=False)
    benchmark_fk = serializers.StringRelatedField(many=False)
    asset_class = serializers.StringRelatedField(many=False)
    product_fk = serializers.StringRelatedField(many=False)

    # created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
    #                                related_name='strategy_created_by')
    # created_date = models.DateTimeField(auto_now_add=True)
    # updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True,
    #                                related_name='strategy_updated_by')
    # updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        model = Strategy
        fields = (
            'id',
            'strategy_name',
            'strategist_fk',
            'benchmark_fk',
            'asset_class',
            'product_fk',
            'created_date',
            'created_by',
            'updated_date',
            'updated_by',
        )

class InvestmentGuidelineOptionsSerializer(serializers.HyperlinkedModelSerializer):
    # strategy = StrategySerializer(many=False, read_only=True)
    strategy = StrategySerializer(many=False, read_only=True)
    investmentguideline = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # investmentguideline = serializers.HyperlinkedRelatedField(many=False,read_only=True,view_name='investmentguideline-detail')
    class Meta:
        model = InvestmentGuidelineOptions
        fields = (
            'id',
            'investmentguideline',
            'strategy',
            'is_enhanced',
            'is_impact',
        )

class InvestmentCounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentCounselor
        fields = (
            'first_name',
            'last_name',
            'created_date',
            'created_by',
            'updated_date',
            'updated_by'
        )

class InvestmentGuidelineSerializer(serializers.HyperlinkedModelSerializer):
    strategies = StrategySerializer(many=True, read_only=True)
    # strategies = DynamicRelationField('InvestmentGuidelineOptionsSerializer',embed=True,many=True, sideloading=True)
    # strategies =
    created_by = serializers.StringRelatedField(many=False)
    updated_by = serializers.StringRelatedField(many=False)
    investment_counselor = InvestmentCounselorSerializer (many=False, read_only=True)

    class Meta:
        model = InvestmentGuideline
        fields = (
            'id',
            'portfolio_code',
            'investment_counselor',
            'strategies',
            'created_date',
            'created_by',
            'updated_date',
            'updated_by',
        )

class AssetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClass
        fields = (
            'asset_class_name',
            'created_date',
            'created_by',
            'updated_date',
            'updated_by',
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'product_name',
            'created_date',
            'created_by',
            'updated_date',
            'updated_by',
        )

class BenchmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benchmark
        fields = (
            'id',
            'benchmark_name',
            'created_by',
            'created_date',
            'updated_by',
            'updated_date'
        )
    def create(self, validated_data):
        return Benchmark.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.benchmark_name = validated_data.get('benchmark_name', instance.email)




class StrategistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategist
        fields = (
            'id',
            'first_name',
            'last_name',
            'created_by',
            'created_date',
            'updated_by',
            'updated_date'
        )


class StrategySerializer(serializers.HyperlinkedModelSerializer):
    strategist_fk = StrategistSerializer
    benchmark_fk = BenchmarkSerializer
    asset_class = AssetClassSerializer
    product_fk = ProductSerializer
    class Meta:
        model = Strategy
        fields = (
            'id',
            'strategy_name',
            'strategist_fk',
            'benchmark_fk',
            'asset_class',
            'product_fk',
            'created_by',
            'created_date',
            'updated_by',
            'updated_date'
        )


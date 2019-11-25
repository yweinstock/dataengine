# Generated by Django 2.1.13 on 2019-10-11 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20191008_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='assetclass',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='asset_class_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assetclass',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assetclass',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='asset_class_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assetclass',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='benchmark',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='benchmark_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='benchmark',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='benchmark',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='benchmark_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='benchmark',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='investmentcounselor',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investment_counselor_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentcounselor',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investmentcounselor',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investment_counselor_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentcounselor',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='investmentguideline',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investment_guideline_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentguideline',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investment_guideline_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentguidelineoptions',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investment_guideline_options_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentguidelineoptions',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investmentguidelineoptions',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investment_guideline_options_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investmentguidelineoptions',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='strategist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='strategist_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='strategist',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategist',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='strategist_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='strategist',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='strategy_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='strategy',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strategy',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='strategy_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='strategy',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

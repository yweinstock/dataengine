# Generated by Django 2.1.13 on 2019-10-08 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191008_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentguidelineoptions',
            old_name='investmentguideline_id',
            new_name='investmentguideline',
        ),
        migrations.RenameField(
            model_name='investmentguidelineoptions',
            old_name='strategy_id',
            new_name='strategy',
        ),
    ]

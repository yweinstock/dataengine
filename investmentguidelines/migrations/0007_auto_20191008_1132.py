# Generated by Django 2.1.13 on 2019-10-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investmentguidelines', '0006_auto_20191008_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentguideline',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]

# Generated by Django 2.1.13 on 2019-11-25 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('viewflow', '0006_i18n'),
        ('core', '0009_auto_20191118_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='BenchmarkApprovalProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.Process')),
                ('approved', models.BooleanField(default=False)),
                ('benchmark', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Benchmark')),
            ],
            options={
                'verbose_name_plural': 'Benchmark approval process list',
                'permissions': [('workflow.benchmark.can_start_request', 'Can benchmark approval process')],
            },
            bases=('viewflow.process',),
        ),
        migrations.CreateModel(
            name='BenchmarkApprovalTask',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('viewflow.task',),
        ),
    ]

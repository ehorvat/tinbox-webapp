# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('color', models.CharField(max_length=200)),
                ('color_cost', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Finish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finish', models.CharField(max_length=200)),
                ('finish_cost', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('quantity_cost', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rounded',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rounded', models.CharField(max_length=1, choices=[(b'y', b'Yes'), (b'n', b'No')])),
                ('rounded_cost', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turnaround', models.CharField(max_length=200)),
                ('turnaround_cost', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
            ],
        ),
    ]

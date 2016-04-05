# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20160214_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='customs.Color', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantities',
            field=models.ManyToManyField(to='customs.Quantity', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='turnarounds',
            field=models.ManyToManyField(to='customs.Shipping', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20160212_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cost_per_unit',
        ),
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=models.ManyToManyField(to='customs.Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='finishes',
            field=models.ManyToManyField(to='customs.Finish'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantities',
            field=models.ManyToManyField(to='customs.Quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='turnarounds',
            field=models.ManyToManyField(to='customs.Shipping'),
        ),
    ]

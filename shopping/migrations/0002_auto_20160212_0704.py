# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='rounded_cost',
            field=models.DecimalField(default=0.0, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='rounded',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

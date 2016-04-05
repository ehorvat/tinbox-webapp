# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20160212_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rounded',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rounded_cost',
            field=models.DecimalField(default=1.0, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]

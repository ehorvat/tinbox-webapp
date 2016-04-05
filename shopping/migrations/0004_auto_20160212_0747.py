# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_remove_cartitem_rounded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='rounded_cost',
            field=models.DecimalField(default=0.0, null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]

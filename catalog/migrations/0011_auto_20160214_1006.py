# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20160214_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='finishes',
            field=models.ManyToManyField(to='customs.Finish', blank=True),
        ),
    ]

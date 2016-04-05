# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_rounded'),
        ('customs', '0002_auto_20160212_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounded',
            name='product',
            field=models.ForeignKey(default=1, to='catalog.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rounded',
            name='rounded',
            field=models.BooleanField(),
        ),
    ]

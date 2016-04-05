# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_category_category_image'),
        ('customs', '0003_auto_20160212_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='rounded',
            name='category',
            field=models.ForeignKey(blank=True, to='catalog.Category', null=True),
        ),
        migrations.AlterField(
            model_name='rounded',
            name='product',
            field=models.ForeignKey(blank=True, to='catalog.Product', null=True),
        ),
    ]

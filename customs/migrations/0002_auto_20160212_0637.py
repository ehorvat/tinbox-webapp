# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rounded',
            name='rounded',
            field=models.ForeignKey(to='catalog.Product'),
        ),
    ]

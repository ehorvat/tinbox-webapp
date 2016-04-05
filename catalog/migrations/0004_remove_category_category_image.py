# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_rounded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20160212_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='rounded',
        ),
    ]

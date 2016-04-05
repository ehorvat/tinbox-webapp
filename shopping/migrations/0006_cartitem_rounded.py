# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20160212_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='rounded',
            field=models.NullBooleanField(),
        ),
    ]

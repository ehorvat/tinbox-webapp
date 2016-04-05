# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20160212_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rounded_internal',
            new_name='rounded',
        ),
        migrations.RemoveField(
            model_name='product',
            name='chose_rounded',
        ),
    ]

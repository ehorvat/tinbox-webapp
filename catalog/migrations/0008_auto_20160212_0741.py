# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20160212_0706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='rounded',
            new_name='rounded_internal',
        ),
        migrations.AddField(
            model_name='product',
            name='chose_rounded',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

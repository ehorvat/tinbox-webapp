# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=200)),
                ('category_image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_dimensions', models.CharField(max_length=200)),
                ('cost_per_unit', models.DecimalField(max_digits=6, decimal_places=2)),
                ('product_image', models.ImageField(upload_to=b'static/images/')),
                ('category', models.ForeignKey(to='catalog.Category')),
                ('colors', models.ManyToManyField(to='customs.Color', blank=True)),
                ('finishes', models.ManyToManyField(to='customs.Finish', blank=True)),
                ('quantities', models.ManyToManyField(to='customs.Quantity', blank=True)),
                ('rounded', models.OneToOneField(null=True, blank=True, to='customs.Rounded')),
                ('turnarounds', models.ManyToManyField(to='customs.Shipping', blank=True)),
            ],
        ),
    ]

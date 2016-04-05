# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('final_cost', models.DecimalField(max_digits=6, decimal_places=2)),
                ('color', models.ForeignKey(to='customs.Color')),
                ('finish', models.ForeignKey(to='customs.Finish')),
                ('product', models.ForeignKey(to='catalog.Product')),
                ('quantity', models.ForeignKey(to='customs.Quantity')),
                ('rounded', models.ForeignKey(blank=True, to='customs.Rounded', null=True)),
                ('shipping', models.ForeignKey(blank=True, to='customs.Shipping', null=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('charge_id', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
            ],
        ),
    ]

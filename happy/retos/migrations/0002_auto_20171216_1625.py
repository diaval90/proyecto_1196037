# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-12-16 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona_reto',
            name='nombre_grupo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reto',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('incativo', 'Inactivo')], default='Activo', max_length=50),
        ),
    ]

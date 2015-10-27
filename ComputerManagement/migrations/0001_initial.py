# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_dispositivo', models.IntegerField()),
                ('nombre_dispositivo', models.CharField(max_length=200)),
                ('fabricante', models.CharField(max_length=200)),
                ('caracteristicas', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_informe', models.IntegerField()),
                ('detalles', models.CharField(max_length=400)),
                ('dispositivo', models.ForeignKey(to='ComputerManagement.Dispositivo')),
            ],
        ),
    ]

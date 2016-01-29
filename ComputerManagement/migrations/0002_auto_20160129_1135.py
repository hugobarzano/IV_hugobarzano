# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_donacion', models.IntegerField()),
                ('nombre_solicitante', models.CharField(max_length=200)),
                ('direcion', models.CharField(max_length=200)),
                ('detalles', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 1, 29, 11, 35, 20, 360368, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donacion',
            name='dispositivo',
            field=models.ForeignKey(to='ComputerManagement.Dispositivo'),
        ),
    ]

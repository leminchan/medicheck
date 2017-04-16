# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20170415_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date_ended',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date end'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='date_started',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date start'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='note',
            name='note_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient'),
        ),
    ]
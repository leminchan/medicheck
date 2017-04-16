# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20170415_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_type',
            field=models.CharField(choices=[('Perscription', 'Perscription'), ('Bloodwork', 'Bloodwork'), ('Allergy', 'Allergy'), ('CT', 'Cat Scan'), ('Additional Notes', 'Additional Notes')], default='Additional Notes', max_length=30),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-16 04:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0006_auto_20160616_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='convite',
            name='observer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observers', to='perfis.ConviteObserver'),
        ),
        migrations.AlterField(
            model_name='conviteobserver',
            name='convite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfis.Convite'),
        ),
        migrations.AddField(
            model_name='conviteobserver',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='publishers', to='perfis.Publisher'),
            preserve_default=False,
        ),
    ]

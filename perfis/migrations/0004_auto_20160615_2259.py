# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-15 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_perfil_contatos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConviteObserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convite', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='perfis.Convite')),
            ],
        ),
        migrations.AddField(
            model_name='convite',
            name='observer',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='perfis.ConviteObserver'),
        ),
    ]

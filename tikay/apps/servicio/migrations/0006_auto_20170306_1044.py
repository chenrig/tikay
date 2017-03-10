# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0005_auto_20170303_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Informacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_titulo', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('categoria_link', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('enlace_titulo', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('enlace_link', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('testigo_texto', models.CharField(blank=True, default=' ', max_length=400, null=True)),
                ('testigo_autor', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('testigo_link', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('ult_actualizacion_titulo', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('ult_actualizacion_texto', models.CharField(blank=True, default=' ', max_length=400, null=True)),
                ('ult_actualizacion_link', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('video_titulo', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('video_sub_titulo', models.CharField(blank=True, default=' ', max_length=100, null=True)),
                ('video_texto', models.CharField(blank=True, default=' ', max_length=400, null=True)),
                ('video_link', models.CharField(blank=True, default='#', max_length=100, null=True)),
                ('video_imagen', models.ImageField(upload_to='imagens')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Actualizacion',
        ),
    ]
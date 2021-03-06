# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JenkinsServerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('ip', models.CharField(max_length=15, unique=True, verbose_name='ip')),
                ('port', models.CharField(max_length=5, verbose_name='port')),
            ],
            options={
                'verbose_name': 'jenkins_server_profile',
                'verbose_name_plural': 'jenkins_server_profiles',
                'db_table': 'jenkins_servers_profiles',
            },
        ),
        migrations.CreateModel(
            name='ServerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('config', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'server_profile',
                'verbose_name_plural': 'server_profiles',
                'db_table': 'servers_profiles',
            },
        ),
        migrations.CreateModel(
            name='TemplateServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('parameters', models.TextField(verbose_name='parameters')),
            ],
            options={
                'verbose_name': 'server_template',
                'verbose_name_plural': 'servers_templates',
                'db_table': 'servers_templates',
            },
        ),
        migrations.AddField(
            model_name='serverprofile',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servers.TemplateServer'),
        ),
    ]

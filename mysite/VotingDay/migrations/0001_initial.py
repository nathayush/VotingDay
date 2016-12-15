# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=100)),
                ('candidate1', models.CharField(max_length=50)),
                ('candidate2', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate3', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate4', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate5', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate6', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate7', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate8', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate9', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate10', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate11', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate12', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate13', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate14', models.CharField(blank=True, max_length=50, null=True)),
                ('candidate15', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('userid', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalvotes', models.IntegerField(default=0)),
                ('vote1', models.IntegerField(default=0)),
                ('vote2', models.IntegerField(default=0)),
                ('vote3', models.IntegerField(default=0)),
                ('vote4', models.IntegerField(default=0)),
                ('vote5', models.IntegerField(default=0)),
                ('vote6', models.IntegerField(default=0)),
                ('vote7', models.IntegerField(default=0)),
                ('vote8', models.IntegerField(default=0)),
                ('vote9', models.IntegerField(default=0)),
                ('vote10', models.IntegerField(default=0)),
                ('vote11', models.IntegerField(default=0)),
                ('vote12', models.IntegerField(default=0)),
                ('vote13', models.IntegerField(default=0)),
                ('vote14', models.IntegerField(default=0)),
                ('vote15', models.IntegerField(default=0)),
                ('partyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VotingDay.Candidate')),
            ],
        ),
    ]
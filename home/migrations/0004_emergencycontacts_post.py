# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-07-26 10:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contacts', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('neighborhood_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('post_description', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('post_hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Neighborhood')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

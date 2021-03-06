# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pekka', '0002_questionvotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=2000)),
                ('answer_time', models.DateTimeField()),
                ('is_good_answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pekka.Question')),
            ],
        ),
    ]

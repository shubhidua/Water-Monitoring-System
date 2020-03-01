# Generated by Django 2.2.10 on 2020-03-01 08:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardware',
            name='id',
        ),
        migrations.RemoveField(
            model_name='hardware',
            name='location',
        ),
        migrations.AddField(
            model_name='hardware',
            name='latitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hardware',
            name='longitude',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='hardware_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hardware',
            name='water_level',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

# Generated by Django 3.1.2 on 2021-12-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20211202_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='max_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statbuff',
            name='buff',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

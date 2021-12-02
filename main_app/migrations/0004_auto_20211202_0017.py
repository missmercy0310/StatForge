# Generated by Django 3.1.2 on 2021-12-02 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rpg_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rpg',
            name='classes_name',
            field=models.CharField(default='Classes', max_length=500),
        ),
        migrations.AlterField(
            model_name='rpg',
            name='entities_name',
            field=models.CharField(default='Playable Entities', max_length=500),
        ),
        migrations.AlterField(
            model_name='rpg',
            name='stats_name',
            field=models.CharField(default='Stats', max_length=500),
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rpg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rpg')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rpg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rpg')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]

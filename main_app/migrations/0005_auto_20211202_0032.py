# Generated by Django 3.1.2 on 2021-12-02 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20211202_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('classification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.classification')),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('class_options', models.ManyToManyField(through='main_app.ClassOption', to='main_app.Classification')),
                ('rpg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.rpg')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='classoption',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.entity'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-17 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeLimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=300)),
                ('day_start', models.DateField()),
                ('day_end', models.DateField()),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MovieFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('allowed_age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.agelimit')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
                ('movie_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movieformat')),
            ],
        ),
        migrations.CreateModel(
            name='ShowTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start', models.TimeField()),
                ('session_end', models.TimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.cinemas')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
        ),
    ]

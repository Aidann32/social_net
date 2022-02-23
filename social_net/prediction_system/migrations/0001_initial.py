# Generated by Django 4.0 on 2022-02-20 17:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0002_relationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olympiad_participation', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('scholarship', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('school', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('fav_sub', models.PositiveIntegerField(choices=[(1, 'Математика'), (2, 'Любая другая точная наука'), (3, 'История/География'), (4, 'Любой язык')])),
                ('projects', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('grasping_power', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('sport_time', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('sport_medals', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('sport_career', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('sport_active', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('fantastic_arts', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да')])),
                ('won_arts', models.PositiveIntegerField(choices=[(0, 'Нет'), (1, 'Да'), (2, 'Возможно')])),
                ('time_art', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('prediction', models.CharField(blank=True, max_length=200)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]
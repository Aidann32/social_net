# Generated by Django 4.0 on 2022-02-23 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
        ('prediction_system', '0003_alter_profiledata_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
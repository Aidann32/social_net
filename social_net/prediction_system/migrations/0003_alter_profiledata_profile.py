# Generated by Django 4.0 on 2022-02-23 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_relationship'),
        ('prediction_system', '0002_alter_profiledata_fantastic_arts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]

# Generated by Django 3.0 on 2020-01-08 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tower_app', '0005_auto_20200108_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='playerID',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tower_app.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='Room q', max_length=64),
        ),
    ]

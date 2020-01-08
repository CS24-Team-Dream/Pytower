# Generated by Django 3.0 on 2020-01-08 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tower_app', '0003_auto_20200107_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=64)),
                ('strength', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='uuid',
        ),
        migrations.AddField(
            model_name='player',
            name='HP',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(default='Room N', max_length=64),
        ),
        migrations.AlterField(
            model_name='player',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tower_app.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='down',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='room',
            name='left',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='room',
            name='right',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='room',
            name='up',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('playerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tower_app.Player')),
            ],
        ),
    ]

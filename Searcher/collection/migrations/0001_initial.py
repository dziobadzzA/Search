# Generated by Django 4.0.1 on 2022-10-26 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vm', models.IntegerField()),
                ('view', models.IntegerField()),
                ('information', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='param_radio_device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='radio_device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_radio_device', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ship_class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_class', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ship_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ship_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ship_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='table_radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_value', models.FloatField()),
                ('param_radio_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.param_radio_device')),
                ('radio_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.radio_device')),
            ],
        ),
        migrations.CreateModel(
            name='ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.ship_class')),
                ('ship_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.ship_name')),
                ('ship_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.ship_place')),
                ('ship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.ship_type')),
            ],
        ),
    ]

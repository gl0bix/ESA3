# Generated by Django 4.0.4 on 2022-05-01 11:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import teahouse.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=60)),
                ('region', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Preperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaware', models.CharField(max_length=60)),
                ('description', models.TextField(blank=True, max_length=500, validators=[django.core.validators.MaxLengthValidator(500)])),
                ('gramms_per_100ml', models.IntegerField()),
                ('steepings', models.IntegerField()),
                ('steeptime_in_sec', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('category', models.CharField(choices=[{'tag': teahouse.models.TeaCategory['GREEN'], 'value': 'Green'}, {'tag': teahouse.models.TeaCategory['BLACK'], 'value': 'Black'}, {'tag': teahouse.models.TeaCategory['OOLONG'], 'value': 'Oolong'}, {'tag': teahouse.models.TeaCategory['SHENG_PUER'], 'value': "Sheng Pu'er"}, {'tag': teahouse.models.TeaCategory['SHU_PUER'], 'value': "Shu Pu'er"}, {'tag': teahouse.models.TeaCategory['WHITE'], 'value': 'White'}, {'tag': teahouse.models.TeaCategory['AGED_WHITE'], 'value': 'Aged White'}], max_length=20)),
                ('cultivar', models.CharField(max_length=60)),
                ('harvested', models.DateField()),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teahouse.origin')),
                ('preperation', models.ManyToManyField(to='teahouse.preperation')),
            ],
        ),
    ]
# Generated by Django 2.2.8 on 2021-04-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid19API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidreport',
            name='percentage_population_infected',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='covidreport',
            name='recovery_rate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

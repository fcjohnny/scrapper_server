# Generated by Django 2.0.4 on 2018-04-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgm_scrapper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='room_date',
            field=models.DateField(verbose_name='room date'),
        ),
    ]

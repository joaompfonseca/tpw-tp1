# Generated by Django 3.1.2 on 2022-11-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20221110_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuit',
            name='length',
            field=models.FloatField(),
        ),
    ]
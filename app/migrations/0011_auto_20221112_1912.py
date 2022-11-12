# Generated by Django 3.1.2 on 2022-11-12 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20221110_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='pilot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='app.pilot'),
        ),
        migrations.AlterField(
            model_name='circuit',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.country'),
        ),
        migrations.AlterField(
            model_name='circuit',
            name='last_winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.pilot'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.team'),
        ),
        migrations.AlterField(
            model_name='race',
            name='circuit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='app.circuit'),
        ),
        migrations.AlterField(
            model_name='result',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.pilot'),
        ),
        migrations.AlterField(
            model_name='result',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.race'),
        ),
        migrations.AlterField(
            model_name='teamleader',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='app.team'),
        ),
    ]
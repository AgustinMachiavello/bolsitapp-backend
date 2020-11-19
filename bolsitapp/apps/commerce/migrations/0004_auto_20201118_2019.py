# Generated by Django 3.1.3 on 2020-11-18 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0003_auto_20201118_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='close_time',
            field=models.TimeField(null=True, verbose_name='Close time'),
        ),
        migrations.AddField(
            model_name='store',
            name='imageURL',
            field=models.URLField(null=True, verbose_name='imageURL'),
        ),
        migrations.AddField(
            model_name='store',
            name='open_time',
            field=models.TimeField(null=True, verbose_name='Open time'),
        ),
    ]

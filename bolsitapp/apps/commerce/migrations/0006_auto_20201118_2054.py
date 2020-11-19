# Generated by Django 3.1.3 on 2020-11-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0005_auto_20201118_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'verbose_name': 'Purchase', 'verbose_name_plural': 'Purchases'},
        ),
        migrations.RemoveField(
            model_name='store',
            name='closeTime',
        ),
        migrations.RemoveField(
            model_name='store',
            name='description',
        ),
        migrations.RemoveField(
            model_name='store',
            name='imageURL',
        ),
        migrations.RemoveField(
            model_name='store',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='store',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='store',
            name='openTime',
        ),
        migrations.AddField(
            model_name='branch',
            name='closeTime',
            field=models.TimeField(null=True, verbose_name='Close time'),
        ),
        migrations.AddField(
            model_name='branch',
            name='description',
            field=models.CharField(max_length=100, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='branch',
            name='imageURL',
            field=models.URLField(null=True, verbose_name='imageURL'),
        ),
        migrations.AddField(
            model_name='branch',
            name='latitude',
            field=models.FloatField(null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='branch',
            name='longitude',
            field=models.FloatField(null=True, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='branch',
            name='openTime',
            field=models.TimeField(null=True, verbose_name='Open time'),
        ),
    ]
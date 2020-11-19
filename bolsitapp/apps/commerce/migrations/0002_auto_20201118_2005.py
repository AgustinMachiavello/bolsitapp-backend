# Generated by Django 3.1.3 on 2020-11-18 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='latitude',
            field=models.IntegerField(null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='store',
            name='longitude',
            field=models.IntegerField(null=True, verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]

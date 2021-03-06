# Generated by Django 3.1.3 on 2020-11-18 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commerce', '0010_auto_20201118_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Bag name'),
        ),
        migrations.AlterField(
            model_name='bag',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]

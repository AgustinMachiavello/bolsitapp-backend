# Generated by Django 3.1.3 on 2020-11-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0011_auto_20201118_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bag',
            name='name',
            field=models.CharField(default='Nueva bolsa', max_length=30, verbose_name='Bag name'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0007_auto_20201118_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name='Bag name'),
        ),
    ]

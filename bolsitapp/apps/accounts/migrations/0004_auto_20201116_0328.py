# Generated by Django 3.1.3 on 2020-11-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201116_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='postal_code',
            field=models.PositiveIntegerField(verbose_name='Postal Code'),
        ),
    ]

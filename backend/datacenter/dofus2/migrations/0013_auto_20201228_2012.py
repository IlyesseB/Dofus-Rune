# Generated by Django 3.1.4 on 2020-12-28 19:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dofus2', '0012_itemprice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

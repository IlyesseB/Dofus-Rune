# Generated by Django 3.1.4 on 2020-12-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dofus2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]

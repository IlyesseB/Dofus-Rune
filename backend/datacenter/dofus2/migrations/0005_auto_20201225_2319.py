# Generated by Django 3.1.4 on 2020-12-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dofus2', '0004_auto_20201225_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristic',
            options={'ordering': ['category', '-weight', 'id']},
        ),
        migrations.AlterField(
            model_name='itemeffect',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='itemseteffect',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mounteffect',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spell',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spellstate',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spellstateeffect',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
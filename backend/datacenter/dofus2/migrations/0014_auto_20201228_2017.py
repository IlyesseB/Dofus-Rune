# Generated by Django 3.1.4 on 2020-12-28 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dofus2', '0013_auto_20201228_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='item',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='dofus2.item'),
        ),
    ]

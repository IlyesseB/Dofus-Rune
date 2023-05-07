# Generated by Django 3.1.4 on 2020-12-28 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dofus2', '0007_auto_20201227_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPrice',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='dofus2.item')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servers', to='dofus2.server')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astronomical_objects', '0002_auto_20210405_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notstarobject',
            name='orbital_parent',
            field=models.CharField(default=None, max_length=50, verbose_name='Orbital parent'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_vehiculo_subasta_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo_subasta',
            name='cc_propietario',
            field=models.IntegerField(blank=True, null=True, verbose_name='cc-propietario'),
        ),
    ]
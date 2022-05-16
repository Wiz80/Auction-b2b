# Generated by Django 4.0.3 on 2022-04-29 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=20, verbose_name='categoria')),
                ('marca', models.CharField(max_length=20, verbose_name='marca')),
                ('modelo', models.CharField(max_length=20, verbose_name='modelo')),
                ('año', models.IntegerField(max_length=4, verbose_name='año')),
                ('kilometraje', models.IntegerField(max_length=30, verbose_name='kilometraje')),
                ('motor', models.CharField(max_length=20, null=True, verbose_name='motor')),
                ('cilindraje', models.CharField(max_length=20, null=True, verbose_name='cilindraje')),
                ('combustible', models.CharField(max_length=20, null=True, verbose_name='combustible')),
                ('placa', models.CharField(max_length=6, verbose_name='placa')),
                ('color', models.CharField(max_length=20, null=True, verbose_name='color')),
                ('soat', models.CharField(max_length=2, verbose_name='soat')),
                ('fecha_soat', models.CharField(max_length=20, null=True, verbose_name='fecha_soat')),
                ('tecno', models.CharField(max_length=2, verbose_name='tecno')),
                ('fecha_tecno', models.CharField(max_length=20, null=True, verbose_name='fecha_tecno')),
                ('propietario', models.CharField(max_length=100, null=True, verbose_name='propietario')),
                ('phone_propietario', models.CharField(max_length=10, null=True, verbose_name='phone_propietario')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.cuenta')),
            ],
        ),
    ]
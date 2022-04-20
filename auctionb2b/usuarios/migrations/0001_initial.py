# Generated by Django 4.0.3 on 2022-04-11 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateTimeField(verbose_name='Fecha_Nacimiento')),
                ('cc', models.IntegerField(verbose_name='cc')),
                ('departamento', models.CharField(max_length=80, verbose_name='Departamento')),
                ('ciudad', models.CharField(max_length=80, verbose_name='Ciudad')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='URL')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='usuarios/pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cuenta',
            },
        ),
    ]

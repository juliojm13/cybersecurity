# Generated by Django 3.2.12 on 2022-11-26 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha del diagnostico')),
                ('gr', models.BigIntegerField(default=0, verbose_name='gestion de riesgos')),
                ('ga', models.BigIntegerField(default=0, verbose_name='gestion de activos')),
                ('gia', models.BigIntegerField(default=0, verbose_name='gestion de identidad y acceso')),
                ('gav', models.BigIntegerField(default=0, verbose_name='gestion de amenazas y vulnerabilidades')),
                ('cea', models.BigIntegerField(default=0, verbose_name='conciencia del estado actual')),
                ('iic', models.BigIntegerField(default=0, verbose_name='intercambio de informacion y comunicaciones')),
                ('ri', models.BigIntegerField(default=0, verbose_name='respuesta a incidentes')),
                ('gde', models.BigIntegerField(default=0, verbose_name='gestion de dependencias externas')),
                ('cp', models.BigIntegerField(default=0, verbose_name='capacitacion del personal')),
                ('gpc', models.BigIntegerField(default=0, verbose_name='gestion de programa de ciberseguridad')),
            ],
        ),
    ]

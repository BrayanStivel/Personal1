# Generated by Django 5.1 on 2024-08-30 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Football', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='equipo',
            table='Equipos',
        ),
        migrations.AlterModelTable(
            name='posicion',
            table='Posiciones',
        ),
    ]

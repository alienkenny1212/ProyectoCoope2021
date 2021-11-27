# Generated by Django 2.2.24 on 2021-11-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('CUI', models.CharField(max_length=13)),
                ('born_date', models.DateField()),
                ('Genre', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('Afiliacion_date', models.DateField()),
                ('Genre', models.CharField(max_length=9)),
                ('Codigo_Socio', models.CharField(max_length=100)),
                ('Cantidad_propiedad', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('CUI', models.CharField(max_length=13)),
                ('FechaNac', models.DateField()),
                ('Genre', models.CharField(max_length=10)),
                ('User', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Puesto', models.CharField(max_length=60)),
                ('Estado', models.CharField(max_length=60)),
            ],
        ),
    ]

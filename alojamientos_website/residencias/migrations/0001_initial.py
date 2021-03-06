# Generated by Django 3.0.3 on 2020-02-17 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0002_auto_20200217_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion_principal', models.CharField(max_length=50)),
                ('direccion_secundaria', models.CharField(max_length=50)),
                ('barrio', models.CharField(max_length=25)),
                ('cantidad_de_lugarares', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('id_arrendador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Usuario')),
                ('id_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residencias.Departamento')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-17 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=25)),
                ('segundo_nombre', models.CharField(max_length=25, null=True)),
                ('primer_apellido', models.CharField(max_length=25)),
                ('segundo_apellido', models.CharField(max_length=25, null=True)),
                ('email', models.CharField(max_length=80)),
                ('es_arrendador', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('FIAT', 'Fiat'), ('CHEVROLET', 'Chevrolet'), ('FORD', 'Ford'), ('TOYOTA', 'Toyota')], default='Ford', max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('s_carroceria', models.CharField(max_length=50, verbose_name='Serial Carrocería')),
                ('s_motor', models.CharField(max_length=50, verbose_name='Serial Motor')),
                ('categoria', models.CharField(choices=[('PARTICULAR', 'Particular'), ('TRANSPORTE', 'Transporte'), ('CARGA', 'Carga')], default='Particular', max_length=20, verbose_name='Categoría')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'ordering': ['categoria']},
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
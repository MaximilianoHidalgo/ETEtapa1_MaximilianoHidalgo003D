# Generated by Django 3.2.4 on 2021-07-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreenPanda', '0009_alter_registro_monedapago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomoneda',
            name='idMoneda',
            field=models.CharField(max_length=1, primary_key=True, serialize=False, verbose_name='Id de Moneda'),
        ),
    ]

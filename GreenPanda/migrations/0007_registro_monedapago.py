# Generated by Django 3.2.4 on 2021-07-07 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GreenPanda', '0006_remove_tipomoneda_monedapago'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='MonedaPago',
            field=models.ForeignKey(default='Dólares', on_delete=django.db.models.deletion.CASCADE, to='GreenPanda.tipomoneda'),
        ),
    ]
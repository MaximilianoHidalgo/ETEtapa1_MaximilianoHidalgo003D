# Generated by Django 3.2.4 on 2021-07-07 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GreenPanda', '0008_alter_registro_monedapago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='MonedaPago',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='GreenPanda.tipomoneda'),
        ),
    ]
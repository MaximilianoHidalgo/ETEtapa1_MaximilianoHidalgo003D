# Generated by Django 3.2.4 on 2021-07-07 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GreenPanda', '0010_alter_tipomoneda_idmoneda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='MonedaPago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GreenPanda.tipomoneda'),
        ),
        migrations.AlterField(
            model_name='tipomoneda',
            name='idMoneda',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Moneda'),
        ),
    ]
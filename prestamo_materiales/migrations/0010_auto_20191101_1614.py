# Generated by Django 2.2.1 on 2019-11-01 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamo_materiales', '0009_pedido_devuelto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['-fecha'], 'verbose_name': 'pedido', 'verbose_name_plural': 'pedidos'},
        ),
    ]

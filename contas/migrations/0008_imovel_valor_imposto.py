# Generated by Django 2.2.4 on 2020-02-09 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_remove_imovel_valor_imposto'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='valor_imposto',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]

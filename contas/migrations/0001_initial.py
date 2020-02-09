# Generated by Django 2.2.4 on 2020-02-08 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('endereco', models.CharField(max_length=250)),
                ('area_terreno', models.DecimalField(decimal_places=2, max_digits=5)),
                ('area_construida', models.DecimalField(decimal_places=2, max_digits=5)),
                ('aliquota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_venal_terreno', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_venal_construcao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('aliquota_aplicada', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contas.Clientes')),
            ],
        ),
    ]
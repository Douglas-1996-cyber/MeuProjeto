from django.db import models


class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=250)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    id = models.AutoField(primary_key=True)
    id_proprietario = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=250)
    area_terreno = models.DecimalField(max_digits=5, decimal_places=2)
    area_construida = models.DecimalField(max_digits=5, decimal_places=2)
    area_total = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    aliquota = models.DecimalField(max_digits=5, decimal_places=2)
    valor_venal_terreno = models.DecimalField(max_digits=5, decimal_places=2)
    valor_venal_construcao = models.DecimalField(max_digits=5, decimal_places=2)
    valor_venal_total = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    aliquota_aplicada = models.DecimalField(max_digits=5, decimal_places=2)
    valor_imposto = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return str(self.id_proprietario)




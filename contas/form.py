from django.forms import ModelForm
from .models import Clientes, Imovel


class CadastrarDono(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'endereco']


class CadastrarImovel(ModelForm):
    class Meta:
        model = Imovel
        fields = ['endereco', 'area_terreno', 'area_construida', 'aliquota', 'valor_venal_terreno',
                  'valor_venal_construcao', 'aliquota_aplicada']


class Imposto(ModelForm):
    class Meta:
        model = Imovel
        fields = ['endereco', 'area_terreno', 'area_construida', 'aliquota', 'valor_venal_terreno',
                  'valor_venal_construcao', 'aliquota_aplicada']





from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes, Imovel
from .form import CadastrarDono, CadastrarImovel, Imposto


def clientes_lista(request):
    clientes = Clientes.objects.all()
    return render(request, 'lista_donos.html', {"clientes": clientes})


def imoveis_lista(request):
    imovel = Imovel.objects.all()
    return render(request, 'index.html', {"imovel": imovel})


def cadastrar(request):
    form = CadastrarDono(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listaD')
    return render(request, 'formulario.html', {'form': form})


def cadastrarimovel(request, id):
    cli = get_object_or_404(Clientes, pk=id)
    form = CadastrarImovel(request.POST or None)

    if form.is_valid():
        i = form.save(commit=False)
        i.id_proprietario = cli
        i.save()
        return redirect('listaD')
    return render(request, 'form_imovel.html', {'form': form})


def atualizarimovel(request, id):
    imo = get_object_or_404(Imovel, pk=id)
    form = Imposto(request.POST or None, instance=imo)
    p = Imovel.objects.get(id=id)
    calcareat = p.area_terreno + p.area_construida
    calcvalorvenalt = p.valor_venal_terreno + p.valor_venal_construcao
    o = float(p.aliquota)
    j = float(calcvalorvenalt)
    calcvalori = j * o
    if form.is_valid():
        n = form.save(commit=False)
        n.area_total = calcareat
        n.valor_venal_total = calcvalorvenalt
        n.valor_imposto = calcvalori
        n.save()
        return redirect('listaI')
    return render(request, 'form_imovel.html', {'form': form})


def atualizardono(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    form = CadastrarDono(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listaD')
    return render(request, 'formulario.html', {'form': form})


def deletedono(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    form = CadastrarDono(request.POST or None, instance=cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listaD')
    return render(request, 'confirm_del_cli.html', {'form': form})


def deleteimovel(request, id):
    imo = get_object_or_404(Imovel, pk=id)
    form = CadastrarImovel(request.POST or None, instance=imo)
    if request.method == 'POST':
        imo.delete()
        return redirect('listaI')
    return render(request, 'confirm_del__imovel.html', {'form': form})


def atualizardono(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    form = CadastrarDono(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listaD')
    return render(request, 'formulario.html', {'form': form})


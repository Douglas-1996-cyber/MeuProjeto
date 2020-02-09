"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from .views import imoveis_lista, cadastrar, cadastrarimovel, clientes_lista, atualizardono, \
    atualizarimovel, deletedono, deleteimovel

urlpatterns = [
    path('listaDonos/', clientes_lista, name="listaD"),
    path('listaImoveis/', imoveis_lista, name="listaI"),
    path('cadastrardono/', cadastrar, name='new_dono'),
    path('cadastrarimovel/<int:id>/', cadastrarimovel, name='new_imovel'),
    path('atualizardono/<int:id>/', atualizardono, name='up_dono'),
    path('atualizarimovel/<int:id>/', atualizarimovel, name='up_imovel'),
    path('deletedono/<int:id>/', deletedono, name='del_dono'),
    path('deleteimovel/<int:id>/', deleteimovel, name='del_imovel'),
]


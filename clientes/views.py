from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from DNA.models import Profile, Machine, bdImage
from clientes.models import Cliente
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import xlwt
import csv

@login_required(login_url='/dna/login/')
def register_client(request):
    """
    Função retorna a view de Cadastro de cliente 
    """
    profiles = Profile.objects.filter(user_id= request.user)
    return render(request, 'clientes/register_client.html',  {'profiles': profiles})

@login_required(login_url='/dna/login/')
@csrf_protect
def register_client_submit(request):
    
    user = request.user
    nomeCliente = request.POST.get('name-cliente')
    codigoCliente = request.POST.get('codigo-cliente')
    razaoCliente = request.POST.get('razao-cliente')
    fantasiaCliente = request.POST.get('nome-fantasia')
    cnpj = request.POST.get('cnpj')
    inscricaoCliente = request.POST.get('inscricao-estado')
    tipoInscricao = request.POST.get('tipo-inscricao')
    pais = request.POST.get('pais')
    estadoCliente = request.POST.get('estado')
    cidadeCliente = request.POST.get('cidade')
    enderecoCLiente = request.POST.get('endereco')
    cep = request.POST.get('cep')
    email = request.POST.get('e-mail')
    telCliente = request.POST.get('tel')

    if(nomeCliente == ""):
        messages.error(request,"'Nome do Cliente' é Obrigatorio!")

    if(cnpj == ""):
        messages.error(request,"'CNPJ' do Cliente é Obrigatorio!")

    if(enderecoCLiente == ""):
        messages.error(request,"'Endereço' do Cliente é Obrigatorio!")
        return redirect("/client/register_Client/")
        
    if(codigoCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Codigo do Cliente' vazio")
    
    if(razaoCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Razão Social' do Cliente vazio")       

    if(fantasiaCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Nome Fantasia' do Cliente vazio")

    if(inscricaoCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Inscrição no Estado' do Cliente vazio")

    if(tipoInscricao == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Tipo de Inscrição' do Cliente vazio")

    if(pais == ""):
        messages.warning(request, "Cliente cadastrado com campo 'País' do Cliente vazio")

    if(estadoCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Estado' do Cliente vazio")

    if(cidadeCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Cep' do Cliente vazio")
    if(cep == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Cidade' do Cliente vazio")

    if(email == ""):
        messages.warning(request, "Cliente cadastrado com campo 'E-mail' do Cliente vazio")

    if(telCliente == ""):
        messages.warning(request, "Cliente cadastrado com campo 'Telefone' do Cliente vazio")
        return redirect("/client/register_Client/")


        
        cliente = Cliente.objects.create(clinte_id=user, code=codigoCliente, nameClient=nomeCliente, companyName=razaoCliente,
        nameFantasy=fantasiaCliente, cnpj=cnpj, stateIncentives=inscricaoCliente, typeIncentives=tipoInscricao,
        country=pais, state=estadoCliente, city=cidadeCliente, clientAddress=enderecoCLiente, clientCep=cep,
        mail=email, phone=telCliente )
        return redirect(request, '/client/register_Client/')

    else:
        cliente = Cliente.objects.create( code=codigoCliente, nameClient=nomeCliente, companyName=razaoCliente,
        nameFantasy=fantasiaCliente,cnpj=cnpj,stateIncentives=inscricaoCliente, typeIncentives=tipoInscricao,
        country=pais, state=estadoCliente,    city=cidadeCliente,clientAddress=enderecoCLiente,clientCep=cep,
        mail=email,phone=telCliente )

        messages.success(request, "Cliente Cadastrado com Sucesso!")
        return redirect( '/client/register_Client/')
        
        

   
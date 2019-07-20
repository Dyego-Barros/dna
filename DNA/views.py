from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Machine, bdImage
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import xlwt
import csv



@login_required(login_url='/dna/login/')
def index(request):
    """
    Função retorna a view raiz do sistema 
    """
    return render(request, 'DNA/index.html')

    

def login_user(request):
     """
     Função retorna a view de login do Sitema
     """
     return render(request, 'DNA/login.html')

@login_required(login_url='/dna/login/')
def dashboard(request): 
     """
     Função retona view de administração do Sistema, 
     e faz consulta no database para retonar dados d
     a sessão do usuario logado
     """
     profiles = Profile.objects.filter(user_id= request.user)    
     return render(request, 'DNA/dashboard.html', {'profiles': profiles})
    
def logout_user(request):
     """
     Função realiza o logout do u
     suario do Sitema e encerra 
     sua sessão
     """
     logout(request)
     return redirect('/dna/login/')

@csrf_protect
def login_submit(request):
     """
     Função valida dados informados no login, 
     se existirem ele valida junto ao database e 
     redireciona para administração,
     se não existirem os dados o úsuario permanece 
     na tela de login.
     """
     if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')              
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/dna/dashboard/')
        else:
            messages.error(request, ' Úsuario e senhas invalidos! ')

     return redirect('/dna/login/')     

@login_required(login_url='/dna/login/')
def register(request):
     """
     Função retorna a view de cadastro de Máquinas no Sistema é 
     necessário  estar logado para acessar a view
     """
     profiles = Profile.objects.filter(user_id= request.user)
     return render(request, 'DNA/register.html',  {'profiles': profiles})

@login_required(login_url='/dna/login/')
@csrf_protect
def set_machine(request):
     """
     Nesta função será tartado os dados vindo do Formulario, 
     os dados serão validados e enviados de acordo 
     com a validação 
     da função
     """
     user = request.user
     maquina = request.POST.get('name-maquina')
     descMaquina = request.POST.get('descricao')
     calibracao = request.POST.get('calibracao')
     cidade = request.POST.get('cidade')
     fabrica = request.POST.get('fabrica')
     grupo = request.POST.get('grupo')
     subGrupo = request.POST.get('subgrupo')
     setor = request.POST.get('setor')
     situacao = request.POST.get('situacao')
     fabricante = request.POST.get('fabricante')
     identificacaoTag = request.POST.get('tag')
     numeroSerie = request.POST.get('serie')
     numeroFabricacao = request.POST.get('numero-fabricacao')
     numeroNota = request.POST.get('nf')
     modelo = request.POST.get('modelo')
     numeroPatrimonial = request.POST.get('patrimonio')
     garantia = request.POST.get('garantia')
     responsavel = request.POST.get('responsavel')
     email = request.POST.get('e-mail')
     dataCadastro = request.POST.get('data')  

     


# Aqui é feita a Validação de Campos Obrigatorios do Formulario se os campos não forem preenchidos o a condição não é satifeita 
# Permanecendo a exibir msg de erro ao usuário até que a condição seja satisfeita
     
     if(maquina == ""):         
          messages.error(request, "Campo Nome da é Obrigatorio!")
     if( descMaquina == ""):              
          messages.error(request, "Campo Descrição Completa é Obrigatorio!")
     if( setor == ""):                   
          messages.error(request,"Campo Setor é Obrigatorio!")

     if(subGrupo == ''):                         
          messages.error(request, "Campo Sub Grupo é Obrigatorio!")

     if(situacao == ""):                              
          messages.error(request, "Campo situação é Obrigatorio!")

     if(identificacaoTag == ''):                                   
          messages.error(request,"Campo Identificação / TAG é Obrigatorio!")

     if(dataCadastro == ''):                                        
          messages.error(request, "Campo Data de Cadastro é Obrigatorio!")  
          return redirect("/dna/dashboard/register/")

          #Verifica Se o Objeto já esta cadastrado no  banco de dados 
     try:
          if(Machine.objects.filter(nameMachine=maquina).exists()):        
               messages.error(request, "Máquina Já cadastrada no banco!") 
               return redirect("/dna/dashboard/register/")
     except expression as identifier:
          return redirect("/dna/dashboard/register/")
      
     try:
          if(Machine.objects.filter(identificationTag =identificacaoTag).exists()):        
               messages.error(request, "TAG Já cadastrada no banco!") 
               return redirect("/dna/dashboard/register/")
     except expression as identifier:
          return redirect("/dna/dashboard/register/")


          return redirect("/dna/dashboard/register/")


#Aqui são validados os dados não obrigatorios onde o usuário pode deixar 
# campos em branco porem sera exibido uma msg de falta de dados ao cadastrar a Máquina     
     if(calibracao == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Calibração Vazio!")
     if(cidade == ""):
         messages.warning(request, "Cadastro Máquina Realizado com o campo Cidade Vazio!")
     if(fabrica == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Fabrica Vazio!")
     if(grupo == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Grupo Vazio!")
     if(fabricante == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Fabricante Vazio!")
     if(numeroSerie == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo N° de Série Vazio!")
     if(numeroFabricacao == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Número de Fabricação Vazio!")
     if(numeroNota == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo N° da NF Vazio!")
     if(numeroPatrimonial == ""):
         messages.warning(request, "Cadastro Máquina Realizado com o campo N° de Patrimônio Vazio!")
     if(modelo == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Modelo Vazio!")
     if(garantia == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Garantia Vazio!")
     if(responsavel == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo Responsável Vazio!")
     if(email == ""):
          messages.warning(request, "Cadastro Máquina Realizado com o campo E-mail Vazio!")

          #Cria o objeto maquina no banco de dados com os dados do formulario
          cadastroMaquina = Machine.objects.create(user=user, nameMachine=maquina, descriptionMachine=descMaquina, calibration=calibracao, city=cidade,
          factory=fabrica, group=grupo, subGroup=subGrupo, sector=setor, situation=situacao, manoFacture=fabricante, identificationTag=identificacaoTag,
          serialNumber=numeroSerie, numberManofacturing=numeroFabricacao, numberInvoice=numeroNota, model=modelo, numberPatrimony=numeroPatrimonial,
          warranty=garantia, registrationDate=dataCadastro, responsible=responsavel, email=email)

          #Faz uma busca no campo file enquanto tiver arquivo no campo ele faz o upload dos aquivos para a pasta base
          #e grava o caminho dos arquivos no banco de dados em uma tabela especifica 
          for count, files in enumerate(request.FILES.getlist('files')): 
               def process(f):
                    with open('C:/Users/Dyego/Desktop/DNA-AUTOMATION/DNA_AUTOMATION/image/image/machine/file_'+ str(files), 'wb+') as destination:
                         for chunk in f.chunks():
                              destination.write(chunk)
               process(files)               
               image = bdImage.objects.create(user=user, idmachine= cadastroMaquina, image=files)
          return redirect('/dna/dashboard/register/')
              
     else:
          #Cria o objeto maquina no banco de dados com os dados do formulario
          cadastroMaquina = Machine.objects.create(user=user, nameMachine=maquina, descriptionMachine=descMaquina, calibration=calibracao, city=cidade,
          factory=fabrica, group=grupo, subGroup=subGrupo, sector=setor, situation=situacao, manoFacture=fabricante, identificationTag=identificacaoTag,
          serialNumber=numeroSerie, numberManofacturing=numeroFabricacao, numberInvoice=numeroNota, model=modelo, numberPatrimony=numeroPatrimonial,
          warranty=garantia, registrationDate=dataCadastro, responsible=responsavel, email=email)

     #Faz uma busca no campo file enquanto tiver arquivo no campo ele faz o upload dos aquivos para a pasta base
     #e grava o caminho dos arquivos no banco de dados em uma tabela especifica 
          for count, files in enumerate(request.FILES.getlist('files')): 
               def process(f):
                    with open('C:/Users/Dyego/Desktop/DNA-AUTOMATION/DNA_AUTOMATION/image/image/machine/file_'+ str(files), 'wb+') as destination:
                         for chunk in f.chunks():
                              destination.write(chunk)
               process(files)               
               image = bdImage.objects.create(user=user, idmachine= cadastroMaquina, image=files)

               #image = bdImage.objects.create(user=user, idmachine= cadastroMaquina, image=str(files))


          messages.success(request,"Máquina Cadastrada com Sucesso!")              
          return redirect('/dna/dashboard/register/')



@login_required(login_url='/dna/login/')
def listreport(request):
     """
     Função faz a consulta e retorna o resultado para o template
     como lista e faz a paginação dos resultados da consulta
     """
     profiles = Profile.objects.filter(user_id= request.user) 
     list_reportList = Machine.objects.all().order_by('-id')
     page_default = 10
     page_select = request.POST.get('paginator')
     search = request.POST.get('search')

     if(search):
          reportList = Machine.objects.filter(nameMachine__icontains=search)
          print(reportList)
          return render(request, 'DNA/report.html',{'reportList':reportList, 'profiles':profiles}) 
     

     if(page_select == None):
          paginator = Paginator(list_reportList, page_default)
          page = request.GET.get('page')
          reportList = paginator.get_page(page)
          return render(request, 'DNA/report.html',{'reportList':reportList, 'profiles':profiles})
     else:
          paginator = Paginator(list_reportList, int(page_select))         
          page = request.GET.get('page')
          reportList = paginator.get_page(page)
          return render(request, 'DNA/report.html',{'reportList':reportList, 'profiles':profiles})

     return render(request, 'DNA/report.html',{'reportList':reportList, 'profiles':profiles})
     

     
@login_required(login_url='/dna/login/')
@csrf_protect
def machine_view(request):
     """
     Função pega o id da Máquina que é passada pela url 
     faz a consulta e retorna o resultado para o template
     """
     profiles = Profile.objects.filter(user_id= request.user)
     machineView = request.GET.get('id')
     images = bdImage.objects.filter(idmachine_id=machineView)
     if(machineView):
          machine = Machine.objects.get(id= machineView)
          if(machine.user == request.user):
               return render(request,'DNA/machine_view.html',{'profiles':profiles, 'machine':machine, 'images':images})
     return render(request, 'DNA/machine_view.html',{'profiles':profiles})


@csrf_protect
def machine_view_submit(request):
     """
     Aque é feita a edição e validação de dados 
     das máquinas Cadastradas no Data Base
     """
     user = request.user
     maquina = request.POST.get('name-maquina')
     descMaquina = request.POST.get('descricao')
     calibracao = request.POST.get('calibracao')
     cidade = request.POST.get('cidade')
     fabrica = request.POST.get('fabrica')
     grupo = request.POST.get('grupo')
     subGrupo = request.POST.get('subgrupo')
     setor = request.POST.get('setor')
     situacao = request.POST.get('situacao')
     fabricante = request.POST.get('fabricante')
     identificacaoTag = request.POST.get('tag')
     numeroSerie = request.POST.get('serie')
     numeroFabricacao = request.POST.get('numero-fabricacao')
     numeroNota = request.POST.get('nf')
     modelo = request.POST.get('modelo')
     numeroPatrimonial = request.POST.get('patrimonio')
     garantia = request.POST.get('garantia')
     responsavel = request.POST.get('responsavel')
     email = request.POST.get('e-mail')
     dataCadastro = request.POST.get('data')  
     machine_id = request.POST.get('machine-id')
    


     if(machine_id):#Verifica se Existe o ID da máquina selecionada para edição 
          machine = Machine.objects.get(id=machine_id)#Se o ID existir é realizada a consulta no banco
          images = bdImage.objects.filter(idmachine_id= machine_id) 
     if(images.exists()):
          for image in images:               
               image.delete()   
     
     if(user == machine.user):#Verifica se o úsuario que cadastrou é o mesmo que fara a edição
          machine.nameMachine = maquina
     if(machine.nameMachine == ""):
          messages.error(request, "Campo Nome da é Obrigatorio!")                   
     machine.descriptionMachine = descMaquina     
     if(machine.descriptionMachine == ""):              
          messages.error(request, "Campo Descrição Completa é Obrigatorio!")
     machine.sector = setor     
     if(machine.sector == ""):                   
          messages.error(request,"Campo Setor é Obrigatorio!")
     machine.subGroup = subGrupo     
     if(machine.subGroup == ''):                         
          messages.error(request, "Campo Sub Grupo é Obrigatorio!")
     machine.situation = situacao
     if(machine.situation == ""):                              
          messages.error(request, "Campo situação é Obrigatorio!")
     machine.identificationTag = identificacaoTag     
     if(machine.identificationTag == ''):                                   
          messages.error(request,"Campo Identificação / TAG é Obrigatorio!")
     machine.registrationDate = dataCadastro     
     if( machine.registrationDate == ''):                                        
          messages.error(request, "Campo Data de Alteração é Obrigatorio!")                
          return redirect("/dna/dashboard/report/machine_view/?id=" + str(machine_id))

          
     machine.city = cidade 
     if(cidade == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Cidade Vazio!")
     machine.calibration = calibracao 
     if(calibracao == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Calibração Vazio!")     
     machine.factory = fabrica
     if(fabrica == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Fabrica Vazio!")
     machine.group = grupo
     if(grupo == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Grupo Vazio!")
     machine.manoFacture = fabricante
     if(fabricante == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Fabricante Vazio!")
     machine.serialNumber = numeroSerie
     if(numeroSerie == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo N° de Série Vazio!")
     machine.numberManofacturing = numeroFabricacao
     if(numeroFabricacao == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Número de Fabricação Vazio!")
     machine.numberInvoice = numeroNota
     if(numeroNota == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo N° da NF Vazio!")
     machine.numberPatrimony = numeroPatrimonial
     if(numeroPatrimonial == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo N° de Patrimônio Vazio!")
     machine.model = modelo
     if(modelo == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Modelo Vazio!")
     machine.warranty = garantia
     if(garantia == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Garantia Vazio!")
     machine.responsible = responsavel
     if(responsavel == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo Responsável Vazio!")
     machine.email = email
     if(email == ""):
          messages.warning(request, "Alteração de Máquina Realizado com o campo E-mail Vazio!")
          machine.save()                   
          return redirect("/dna/dashboard/report/machine_view/?id=" + str(machine_id))                  
     
     for files in request.FILES.getlist('files'):
          img= bdImage.objects.create(user=user, idmachine_id= machine_id, image=files)
          
     else:
          machine.save()
          messages.success(request, "Máquina Alterada com sucesso!")
          return redirect("/dna/dashboard/report/machine_view/?id=" + str(machine_id))

     
@login_required(login_url='/dna/login/')
def delete(request, id):
     """
     Função deleta maquina selecionada no template

     """
    
     machine = get_object_or_404(Machine, pk=id)   
     if(machine.user == request.user):
          machine.delete()   
         
     return redirect('/dna/dashboard/report/')

def export_machine_csv(request):
    exportcsv = request.GET.get('id')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Máquina.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Máquina')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id','Nome Máquina', 'Descrição da Máquina', 'Calibração ', 'Cidade',
                      'Fábrica', 'Grupo', 'Sub Grupo', 'Setor',
                      'Situação', 'Fabricação', 'Identificão TAG', 'Número de Série',
                      'Número de Fabricação', 'Número da Nota', 'Modelo', 'Número Patrimonial',
                      'Garantia', 'Data de Registro', 'Responsavel', 'E-mail', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Machine.objects.filter(id=exportcsv).values_list('id','nameMachine', 'descriptionMachine', 'calibration', 'city',
                      'factory', 'group', 'subGroup', 'sector',
                      'situation', 'manoFacture', 'identificationTag', 'serialNumber',
                      'numberManofacturing', 'numberInvoice', 'model', 'numberPatrimony',
                      'warranty', 'registrationDate', 'responsible', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

def export_allMachine_csv(request):   
    maquinas = Machine.objects.all() 
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Todas-as-Máquina.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Todas-as-Máquina')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Id','Nome Máquina', 'Descrição da Máquina', 'Calibração ', 'Cidade',
                      'Fábrica', 'Grupo', 'Sub Grupo', 'Setor',
                      'Situação', 'Fabricação', 'Identificão TAG', 'Número de Série',
                      'Número de Fabricação', 'Número da Nota', 'Modelo', 'Número Patrimonial',
                      'Garantia', 'Data de Registro', 'Responsavel', 'E-mail', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Machine.objects.all().values_list('id','nameMachine', 'descriptionMachine', 'calibration', 'city',
                      'factory', 'group', 'subGroup', 'sector',
                      'situation', 'manoFacture', 'identificationTag', 'serialNumber',
                      'numberManofacturing', 'numberInvoice', 'model', 'numberPatrimony',
                      'warranty', 'registrationDate', 'responsible', 'email')
    print(rows)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response




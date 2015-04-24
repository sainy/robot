from django.shortcuts import render
from django.http import HttpResponse
import models


def index(request):
#    return HttpResponse('Hello, world')
#    ecs_api_url = request.POST['ecs_api_url']
    deploy_sheet = list(models.DeploySheet.objects.all())
    sheet_names = []
    for sheet in deploy_sheet:
        sheet_names.append(sheet.name)
    selected_sheet_name = 'acadci_staging_sha'
    selected_deploy_sheet = models.DeploySheet.objects.get(name='acadci_staging_sha')
    selected_instances = list(selected_deploy_sheet.instances.all())
    selected_deploys = list(selected_deploy_sheet.deploys.all())
    selected_variables = list(selected_deploy_sheet.varibles.all())
    context = {"sheet_names":sheet_names, 
               "selected_sheet_name":selected_sheet_name, 
               "selected_deploy_sheet":selected_deploy_sheet,
               "selected_instances":selected_instances,
               "selected_deploys":selected_deploys,
               "selected_variables":selected_variables
              }

    return render(request, 'deploy/index.html', context)

def addItem(request):
    if not request.POST.has_key('sheet_name'):
        return render(request, 'deploy/index.html')
    context = {"sheet_name": request.POST['sheet_name']}
    return render(request, 'deploy/addItem.html', context)


def saveItem(request):
    #save the new added item into deploy sheet
    instance = request.POST['instance']
    slave_name = request.POST['slave_name']
    uniq_id = request.POST['uniq_id']
    ip_addr = request.POST['ip_addr']
    fqdn = request.POST['fqdn']
    ecs_command = request.POST['ecs_command']
    if not instance or not slave_name or not uniq_id or not ip_addr:
        context = {"sheet_name": request.POST['sheet_name']}
        return render(request, 'deploy/addItem.html', context)
    if not fqdn:
        fqdn = ip_addr
    db_ins = models.Instances.objects.create(Instance=instance, Inst_Name=slave_name, Inst_Id=uniq_id, Inst_Ip=ip_addr, Inst_Fqdn=fqdn, Inst_Cmd=ecs_command)
    db_deploysheet = models.DeploySheet.objects.get(name=request.POST['sheet_name'])
    db_deployship = models.DeployInstanceShip.objects.create(instance=db_ins, sheet=db_deploysheet)
    #then, query the whole db to get the deploy sheet and show
    
#    context = {"sheet_name": request.POST['sheet_name']}
#    return render(request, 'deploy/addItem.html', context)

    return render(request, 'deploy/index.html')


def saveVariable(request):
    sheet_name = ""
    if request.POST.has_key('sheet_name'):
        sheet_name = request.POST['sheet_name']
    context = {"sheet_name": sheet_name}
    return render(request, 'deploy/addItem.html', context)

# Create your views here.

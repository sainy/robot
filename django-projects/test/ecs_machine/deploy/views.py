from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import models

def getAllSheets():
    deploy_sheet = list(models.DeploySheet.objects.all())
    sheet_names = []
    for sheet in deploy_sheet:
        sheet_names.append(sheet.name)
    return sheet_names

def querySheetByName(sheet_name):
    try:
        deploy_sheet = models.DeploySheet.objects.get(name=sheet_name)
    except models.DeploySheet.DoesNotExist:
        return []
    return deploy_sheet


def index(request):
    context = {"sheet_names":getAllSheets()}
    return render(request, 'deploy/index.html', context)


def instance(request, sheet_name):
    check_to_store(request, sheet_name)
    
    deploy_sheet = querySheetByName(sheet_name)
    if not deploy_sheet:
        raise Http404("Deploy Sheet does not exist")
    
    new_item = False
    if request.POST.has_key('new_item'):
        new_item = request.POST['new_item']

    selected_instances = list(deploy_sheet.instances_set.all())

    context = {"sheet_names":getAllSheets(),
                "selected_sheet_name":sheet_name,
                "selected_instances":selected_instances,
                "new_item":new_item
               }

    return render(request, 'deploy/index.html', context)

def check_to_store(request, sheet_name):
    instance=''
    name = ''
    inst_id = ''
    ip_addr = ''
    fqdn = ''
    ecs_cmd = ''
    if request.POST.has_key("instance"):
        instance = request.POST["instance"]
    if request.POST.has_key("name"):
        name = request.POST["name"]
    if request.POST.has_key("id"):
        inst_id = request.POST["id"]
    if request.POST.has_key("ip"):
        ip_addr = request.POST["ip"]
    if request.POST.has_key("fqdn"):
        fqdn = request.POST["fqdn"]
    if request.POST.has_key("cmd"):
        ecs_cmd = request.POST["cmd"]
    sheet = models.DeploySheet.objects.get(name=sheet_name)
    db_ins = models.Instances.objects.create(Instance=instance, Inst_Name=name, Inst_Id=inst_id, Inst_Ip=ip_addr, Inst_Fqdn=fqdn, Inst_Cmd=ecs_cmd, sheet=sheet)


def deploy(request, sheet_name):
    deploy_sheet = querySheetByName(sheet_name)
    if not deploy_sheet:
        raise Http404("Deploy Sheet does not exist")

    new_item = False
    if request.POST.has_key('new_item'):
        new_item = request.POST['new_item']

    selected_deploys = list(deploy_sheet.deploys_set.all())
    
    context = {"sheet_names":getAllSheets(),
               "selected_sheet_name":sheet_name,
               "selected_deploys":selected_deploys,
               "new_item":new_item
              }

    return render(request, 'deploy/deploy.html', context)


def variable(request, sheet_name):
    deploy_sheet = querySheetByName(sheet_name)
    if not deploy_sheet:
        raise Http404("Deploy Sheet does not exist")
    
    new_item = False
    if request.POST.has_key('new_item'):
        new_item = request.POST['new_item']

    selected_variables = list(deploy_sheet.variables_set.all())

    context = {"sheet_names":getAllSheets(),
               "selected_sheet_name":sheet_name,
               "selected_variables":selected_variables,
               "new_item":new_item
              }

    return render(request, 'deploy/variable.html', context)


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
    sheet = models.DeploySheet.objects.get(name=request.POST['sheet_name'])
    db_ins = models.Instances.objects.create(Instance=instance, Inst_Name=slave_name, Inst_Id=uniq_id, Inst_Ip=ip_addr, Inst_Fqdn=fqdn, Inst_Cmd=ecs_command, sheet=sheet)
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

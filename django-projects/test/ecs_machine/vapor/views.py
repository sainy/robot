from django.shortcuts import render
from django.http import HttpResponse

import vapor_api
import os
# Create your views here.

def index(request):
#    return HttpResponse('Hello, world')
#    ecs_api_url = request.POST['ecs_api_url']
    return render(request, 'vapor/index.html')


def query(request):
    ecs_api_url = request.POST['ecs_api_url']
    headers = dict()
    os.environ["ECS_ACCESS_KEY"] = "uAMYOadqsIMbwf6FjDOVe4Kb1RAd3OqGIgi7PfYBkkE6Sn3usRSF_CDRdW2eiU8LwprL-nUUusvPKJcSy4Ohng"
    os.environ["ECS_SECRET_KEY"] = "CqClpqA_OKAmS2eacp0Gf4WmcG4pICYXnRzq9HYnVQhT5mXBzgv87Usx_OPxzY9qFRN6MemX0AC4fMEisU1lVA"
    instance_list = vapor_api.ecs_getInstances(ecs_api_url, headers)


#    context = basic.ecs_request(ecs_api_url, headers)
    #if not context:
    #    context = "You're looks so beautifull"
    #return HttpResponse(str(context))
    context = {'instance_list': instance_list}
    return render(request, 'vapor/cimachine.html', context)
    #return HttpResponse("You're looks so beautifull")

#In this file, we write the wrapper for each ecs vapor api
#In each wrapper, it will call vapor api and do the db job(including store into db and query from db)

import basic
#import models
import db

def ecs_getInstances(ecs_api_url, query_header):
    result = basic.ecs_request(ecs_api_url, query_header)
    if not result:
        return None
    all_instances = db.getAllInstance()
    for instance in all_instances:
        find = False
        for item in result['Items']:
            if instance.InstanceId == item['InstanceId']:
                find = True
                break
        if not find:
            db.deleteInstance(instance)
    for item in result['Items']:
        if item['Name'].lower().rfind('acadci') == -1:
            continue
        if not db.queryInstancebyId(instanceid=item['InstanceId']):
            db.createInstance(InsDict=item)
    return db.getAllInstance()

def ecs_getVolumes(ecs_api_url, query_header):
    result = basic.ecs_request(ecs_api_url, query_header)
    if not result:
        return None
    return result

def getInstances():
    return db.getAllInstance()



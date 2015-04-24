import base64
from datetime import datetime
import hmac
import hashlib
import json
import os
from urllib2 import Request, urlopen
   
#from urllib import urlopen

def get_stored_keys():
    return os.environ["ECS_ACCESS_KEY"], os.environ["ECS_SECRET_KEY"]
    
def get_utc_8601_now_time_str():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
def generate_ecs_signature(ecs_api_url, ecs_secret_key):
    utc_signed_time = get_utc_8601_now_time_str()
    key = ecs_secret_key + utc_signed_time
    data = ecs_api_url.lower()
    hash = hmac.new(key.encode("ascii"), data.encode("ascii"), hashlib.sha1).digest()
    signature = base64.b64encode(hash).decode("ascii").rstrip("\n")
    return utc_signed_time, signature

def isheadervalid(header):
    if 'AccessKey' not in header.keys():
        return False
    if 'Signature' not in header.keys():
        return False
    if 'TimeStamp' not in header.keys():
        return False
    return True

def add_common_param(ecs_api_url, header):
    if isheadervalid(header):
        return header
    ecs_access_key, ecs_secret_key = get_stored_keys()
    utc_signed_time, ecs_signature = generate_ecs_signature(ecs_api_url, ecs_secret_key)
    header['AccessKey'] = ecs_access_key
    header['Signature'] = ecs_signature
    header['TimeStamp'] = utc_signed_time
    return header

def ecs_request(ecs_api_url, headers):
    if not isinstance(headers, dict):
        return None
    add_common_param(ecs_api_url, headers)

    request = Request(ecs_api_url, headers=headers)
#    response = urlopen(ecs_api_url, headers)
    response = urlopen(request)
    try:
        result = json.loads(response.read().decode("utf-8"))
    except:
        return None
    return result




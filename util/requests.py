import json
import requests

base_url = "https://my.tanda.co/api/v2/"

def get(extension, token):
    auth = 'Bearer ' + token.getToken()
    headers = {'Cache-Control': 'no-cache', 'Authorization': auth}
    data = requests.get(base_url + extension, headers=headers)
    return data

def post(extension, params, token):
    auth = 'Bearer ' + token.getToken()
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    requests.post(base_url + extension, params=params, headers=headers)

def put(extension, params, token):
    auth = 'Bearer ' + token.getToken()
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    requests.put(base_url + extension, params=params, headers=headers)

def delete(extension, token):
    auth = 'Bearer ' + token.getToken()
    headers = {'Content-Type': 'application/json', 'Authorization': auth}
    requests.delete(base_url + extension, headers=headers)

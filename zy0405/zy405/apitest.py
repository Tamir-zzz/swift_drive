from django.test import TestCase

# Create your tests here.

import sys
import json
import requests

# 获取domain范围token
def get_domain_token():
    data = {
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "name":"default"
                        },
                        "password": "1234"
                    }
                }
            },
            "scope": {
                "domain": {
                    "name":"default"
                }
            }
        }
    }
    url = "http://192.168.53.105:5000/v3/auth/tokens"
    result = requests.post(url, data=json.dumps(data)).headers.get("X-Subject-Token")
    # 返回的token在 response header 里面
    return result

# domain_token = get_domain_token()
# print(domain_token)



def get_v3_token():
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "domain": {
                            "name": 'default'
                        },
                        "name": 'admin',
                        "password": '1234'
                    }
                }
            },
            "scope": {
                "project": {
                    "domain": {
                        "name": "default"
                    },
                    "name": "admin"
                }
            }
        }
    }
    url = "http://192.168.53.105:5000/v3/auth/tokens"
    result = requests.post(url, data=json.dumps(data))
    # print(result)
    token = result.headers.get("X-Subject-Token")
    # print(token)
    return token

domain_token = get_v3_token()
print(domain_token)

# 获取project范围token
def get_project_token(domain_token):
    data = {
        "auth": {
            "identity": {
                "methods": [
                    "token"
                ],
                "token": {
                    "id": domain_token
                }
            },
            "scope": {
                "project": {
                    "domain": {
                        "name": "default"
                    },
                    "name": "admin"
                }
            }
        }
    }
    url = "http://192.168.53.105:5000/v3/auth/tokens"
    result = requests.post(url, data=json.dumps(data)).headers.get("X-Subject-Token")
    # 返回的token在 response header 里面
    return result

project_token = get_project_token(domain_token)
print(project_token)


def get_projects(damian_token):
    # damian_token = request.GET.seesion['damian_token']
    url = "http://192.168.53.105:5000/v3/projects"
    headers = {"X-Auth-Token": damian_token}
    param = {"format": 'json'}
    resp = requests.get(url, headers=headers, params=param)
    data = resp.json()
    print(data)
    # print(type(data))

    return data

# get_projects(domain_token)

# 列出servers
def servers_list():
    url = "http://192.168.53.105:8774/v2.1/servers"
    headers = {}
    headers["X-Auth-Token"] = project_token
    result = requests.get(url, headers=headers)
    return result

res = servers_list()
print(res)
print(res.json())


# # 列出可用image
# def images_list():
#     url = "http://192.168.53.105:9292/v2/images"
#     headers = {}
#     headers["X-Auth-Token"] = project_token
#     result = requests.get(url, headers=headers)
#     return result

# res = images_list()
# print(res)
# print(res.json())

# # 列出可用flavor
# def flavor_list():
#     url = "http://192.168.53.105:8774/v2.1/flavors"
#     headers = {}
#     headers["X-Auth-Token"] = project_token
#     result = requests.get(url, headers=headers)
#     return result

# res = flavor_list()
# print(res)
# print(res.json())

# # 列出可用flavor
# def flavor_list():
#     url = "http://192.168.53.105:8774/v2.1/flavors"
#     headers = {}
#     headers["X-Auth-Token"] = project_token
#     result = requests.get(url, headers=headers)
#     return result

# res = flavor_list()
# print(res)
# print(res.json())


############
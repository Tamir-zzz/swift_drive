# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render_to_response,RequestContext
import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect


# 获取登陆 token
def get_domain_token(username, passwd):
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
                        "name": username,
                        "password": passwd
                    }
                }
            },
        }
    }
    url = "http://192.168.53.105:35357/v3/auth/tokens"
    result = requests.post(url, data=json.dumps(data))
    # token = result.headers.get("X-Subject-Token")
    return result


# 获取操作容器token
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
    url = "http://192.168.53.105:35357/v3/auth/tokens"
    result = requests.post(url, data=json.dumps(data))
    token = result.headers.get("X-Subject-Token")
    # print(result)
    # print(token)
    return token


# get_v3_token()
# token = get_v3_token()
# print(token)


def get_info(v3_token):
    v3_token = get_v3_token()
    print(v3_token)
    # damian_token = 'gAAAAABihFiJ5WczVfk0R3f9k0F2zDJBACcrO0R-_e2bnyYt9JK_6rBJiqlVTNdJx4TkP2t_1Ay4d6-rpTlmFVGXCWFrF0Ya7aok4VFBiE3760aSPu52l_9xK7jEfp8jj937CNbTRmUCKl8-cLgu4bGIeWm6BjPA-RQF0kQOtUY-R4UMfn_xDUo'
    url = "http://192.168.53.105:5000/info"
    headers = {"X-Auth-Token": v3_token}
    param = {"format": 'json'}
    resp = requests.get(url, headers=headers, params=param)
    data = resp.json()
    print(data)
    # print(type(data))
    return data
# get_info(token)


    # demo1   AUTH_542629b3b00f4a47854f47fd084da3e0/aaaaa/demo8.txt
    # curl -i http://192.168.53.105:8080/v1/AUTH_71dd930094aa458aad94b74d48a3b48b/bb/demo9.txt 
    # -X PUT 
    # -H "X-Auth-Token: gAAAAABkNAYAO41WUWNkv5EjeTebQ2mvRv4BPb8awGPZIONq5U6vhT58WN2IOwGF2kVDqrxjaIj8wyJ83yfuUpfuKCBHyzFlIHF6q0rTvhLf0Oa77XYZGi4UXJEh3dve_xcQPLEifKBwxywHiy2L9oghxqglG12X6hIS0xEUOyfLwHq1BpdTaIk" 
    # -H "X-Copy-From: Ben/demo8.txt" 
    # -H "Content-Length: 0" 
    # -H "X-Copied-From-Account: AUTH_542629b3b00f4a47854f47fd084da3e0"
    # headers["Destination"] = "bb/demo3.jpg"

def get_chare_object():
    token = "gAAAAABkZaNCFR6BvrygtrPsB_MHTHKd2HReNtGkFtZ6bcQFUgsU-C6g0IOMsLN0vWLc1ueXu22dH3GhjX2gJEzDStXS7Zh3PBghgQrDzmp2tGn9lkJxeIzxBYKWFBAE8CvBA7B85YJtediRsK3rA4b4nXhMWHZv3hl6TfvD5TrrlSAZlM6YTp8"
    # token = get_v3_token()
    url = "http://192.168.53.105:8080/v1/AUTH_71dd930094aa458aad94b74d48a3b48b/Ben/demo3.mp4?format=json"
    headers = {}
    headers["X-Auth-Token"] = token
    headers["Content-Length"] = "0"
    headers["X-Copy-From"] = "ggg/demo3.mp4"
    headers["X-Copied-From-Account"] = "AUTH_542629b3b00f4a47854f47fd084da3e0"
    resp = requests.put(url, headers=headers)
    print(resp)
    # data = resp.json()
    # print(data)
    # curl -i $url/bb/demo8.txt -X COPY -H "X-Auth-Token: $token" -H "Destination: aaaaa/demo9.txt" -H "Destination-Account: http://192.168.53.105:8080/v1/AUTH_542629b3b00f4a47854f47fd084da3e0"
    return resp


get_chare_object()
#################################


def login(request):
    return render(request, "login.html")


def loginCheck(request):
    uname = request.POST.get('username')
    # print(uname)
    passwd = request.POST.get('passwd')
    result = get_domain_token(uname, passwd)
    domain_token = result.headers.get("X-Subject-Token")
    v3_token = get_v3_token()

    if result.status_code == 201 or result.status_code == 200:
        # print(v3_token)
        request.session['domain_token'] = domain_token
        request.session['v3_token'] = v3_token
        return render(request, 'index.html')
        # return get_projects_web(request)
        # return redirect(get_counters_web(request))
    else:
        return render(request, 'login.html')
        # return login(request)


# 跳转主页
def index(request):
    # projects_datas = get_projects()
    return render(request, 'index.html')


#################################################

# 获取项目目录 ########################################################

def get_projects(token):
    # v3_token = request.session.get('v3_token')
    v3_token = token
    # damian_token = 'gAAAAABihFiJ5WczVfk0R3f9k0F2zDJBACcrO0R-_e2bnyYt9JK_6rBJiqlVTNdJx4TkP2t_1Ay4d6-rpTlmFVGXCWFrF0Ya7aok4VFBiE3760aSPu52l_9xK7jEfp8jj937CNbTRmUCKl8-cLgu4bGIeWm6BjPA-RQF0kQOtUY-R4UMfn_xDUo'
    url = "http://192.168.53.105:5000/v3/projects"
    headers = {"X-Auth-Token": v3_token}
    param = {"format": 'json'}
    resp = requests.get(url, headers=headers, params=param)
    data = resp.json()
    print(data)
    # print(type(data))

    return data
    # return resp

# get_projects(token)


# 创建项目
def cre_project(request):
    name = request.POST.get('project_name')
    description = request.POST.get('description')
    domain_token = request.session.get("v3_token")
    # project_id = request.POST.get('project_id')
    url = "http://192.168.53.105:5000/v3/projects"
    data = {
        "project": {
            "description": description,
            "domain_id": "f35a42e4bed84bb6aae492b7e2bc8b0f",
            "enabled": True,
            "is_domain": False,
            "name": name,
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)

    return redirect('zy405:projects')


#  更新项目
def update_project(request):
    name = request.POST.get('project_name')
    description = request.POST.get('description')
    domain_token = request.session.get("v3_token")
    project_id = request.POST.get('project_id')
    print(name, description, project_id, domain_token)
    url = "http://192.168.53.105:5000/v3/projects/%s" % (project_id)
    data = {
        "project": {
            "description": description,
            "name": name
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_update = requests.patch(url, data=json.dumps(data), headers=headers)
    print(resp_update)
    return redirect('zy405:projects')

#  删除项目


def del_project(request, project_id):
    domain_token = request.session.get("v3_token")
    # project_id = request.POST.get('project_id')
    url = "http://192.168.53.105:5000/v3/projects/%s" % (project_id)
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_del = requests.delete(url, headers=headers)
    # print(resp_del)
    return redirect('zy405:projects')

# 获取 项目


def projects(request):
    # resp = get_projects(request)
    projects_datas = get_projects(request)
    projects_datas = projects_datas['projects']

    # print(projects_datas)
    # print("aaa")
    # projects_datas = resp.json()
    return render(request, 'projects.html', {'projects_datas': projects_datas})

#############################################################


# 获取 实例
def get_servers(request):
    v3_token = request.session.get('v3_token')
    url = "http://192.168.53.105:8774/v2.1/servers"
    headers = {}
    headers["X-Auth-Token"] = v3_token
    result = requests.get(url, headers=headers)
    result = result.json()
    # print(result)
    return result


# 获取 项目
def servers(request):
    # resp = get_projects(request)
    servers_datas = get_servers(request)
    servers_datas = servers_datas['servers']

    # print(projects_datas)
    # print("aaa")
    # projects_datas = resp.json()
    return render(request, 'servers.html', {'servers_datas': servers_datas})


def cre_servers(request):
    # name = request.POST.get('name')
    domain_token = request.session.get("v3_token")
    # images_id = request.POST.get('images_id')
    url = "http://192.168.53.105:8774/v2.1/servers"
    data = {
        "server": {
            "name": "ddddd",
            "imageRef": "8c0f94ed-8dbc-44e7-840a-a4363aabe7b9",
            "flavorRef": "http://192.168.53.105:8774/v2.1/flavors/1",
            "networks": "auto"
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)
    print("aaa")
    return redirect('zy405:servers')


####################################################
# 获取用户的信息
def get_users(domain_token):
    url = "http://192.168.53.105:5000/v3/users"
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.get(url, headers=headers)
    print("users: ", resp.json())
    # print(resp)
    return resp


# 获取用户列表
def users_list(request):
    domain_token = request.session.get("domain_token", None)
    v3_token = request.session.get("v3_token", None)
    if not(domain_token and v3_token):
        return redirect('zy405:login')

    else:
        resp = get_users(v3_token)
        if resp.status_code == 200:
            request.session["users_list"] = resp.json()
            users_data = resp.json()["users"]
            # print(users_data)
            return render(request, 'users.html', {'users_data': users_data})
        else:
            return redirect('zy405:users')

# 创建用户


def cre_users(request):
    domain_token = request.session.get("v3_token")
    name = request.POST.get('name')
    description = request.POST.get('description')
    email = request.POST.get('email')
    url = "http://192.168.53.105:5000/v3/users"
    data = {
        "user": {
            "name": name,
            "enabled": True,
            "domain_id": "f35a42e4bed84bb6aae492b7e2bc8b0f",
            "description": description,
            "email": email,
            "password": "123456",
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    return redirect('zy405:users')

#  更新用户


def update_users(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    v3_token = request.session.get("v3_token")
    users_id = request.POST.get('user_id')
    email = request.POST.get('email')
    print(email)
    url = "http://192.168.53.105:5000/v3/users/%s" % (users_id)
    data = {
        "user": {
            "description": description,
            "name": name,
            "email": email,
        }
    }
    headers = {}
    headers['X-Auth-Token'] = v3_token
    resp_update = requests.patch(url, data=json.dumps(data), headers=headers)
    print(resp_update)
    return redirect('zy405:users')


#  删除用户
def del_users(request, user_id):
    domain_token = request.session.get("v3_token")
    # users_id = request.POST.get('users_id')
    url = "http://192.168.53.105:5000/v3/users/%s" % (user_id)
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_del = requests.delete(url, headers=headers)
    return redirect('zy405:users')


#######################################

# 获取组的信息
def get_groups(domain_token):
    url = "http://192.168.53.105:5000/v3/groups"
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.get(url, headers=headers)
    datas = resp.json()
    print(datas)
    return resp


# 获取组列表
def groups_list(request):
    domain_token = request.session.get("domain_token")
    v3_token = request.session.get("v3_token")
    if not(domain_token and v3_token):
        return redirect('zy405:login')

    else:
        resp = get_groups(v3_token)

        if resp.status_code == 200:
            groups_datas = resp.json()["groups"]
            return render(request, 'groups.html', {'groups_datas': groups_datas})

        else:
            return redirect('zy405:groups')

# 创建组


def cre_groups(request):
    domain_token = request.session.get("v3_token")
    name = request.POST.get('name')
    description = request.POST.get('description')
    url = "http://192.168.53.105:5000/v3/groups"
    data = {
        "group": {
            "name": name,
            "description": description,
            "domain_id": "f35a42e4bed84bb6aae492b7e2bc8b0f",

        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)
    return redirect('zy405:groups')


#  更新组
def update_groups(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    domain_token = request.session.get("v3_token")
    groups_id = request.POST.get('groups_id')
    url = "http://192.168.53.105:5000/v3/groups/%s" % (groups_id)
    data = {
        "group": {
            "name": name,
            "description": description,
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_update = requests.patch(url, data=json.dumps(data), headers=headers)
    print(resp_update)
    return redirect('zy405:groups')


#  删除组
def del_groups(request, groups_id):
    domain_token = request.session.get("v3_token")
    # groups_id = request.POST.get('groups_id')
    url = "http://192.168.53.105:5000/v3/groups/%s" % (groups_id)
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_del = requests.delete(url, headers=headers)
    return redirect('zy405:groups')

############################################
# 获取角色的信息


def get_roles(domain_token):
    url = "http://192.168.53.105:5000/v3/roles"
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.get(url, headers=headers)
    # print("roles: ",resp.json())
    return resp


# 获取角色列表
def roles_list(request):
    domain_token = request.session.get("domain_token", None)
    v3_token = request.session.get("v3_token", None)
    if not(domain_token and v3_token):
        return redirect('zy405:login')

    else:
        resp = get_roles(v3_token)
        if resp.status_code == 200:
            roles_datas = resp.json()["roles"]
            print(roles_datas)
            return render(request, 'roles.html', {'roles_datas': roles_datas})

        else:
            return redirect('zy405:roles')

# 创建角色


def cre_roles(request):
    domain_token = request.session.get("v3_token")
    name = request.POST.get('name')
    url = "http://192.168.53.105:5000/v3/roles"
    data = {
        "role": {
            "domain_id": None,
            "name": name,
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    # print(resp)
    return redirect('zy405:roles')


#  更新角色
def update_roles(request):
    name = request.POST.get('name')
    domain_token = request.session.get("v3_token")
    roles_id = request.POST.get('roles_id')
    url = "http://192.168.53.105:5000/v3/roles/%s" % (roles_id)
    data = {
        "role": {
            "name": name
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_update = requests.patch(url, data=json.dumps(data), headers=headers)
    # print(resp_update)
    return redirect('zy405:roles')


#  删除角色
def del_roles(request, roles_id):
    domain_token = request.session.get("v3_token")
    # roles_id = request.POST.get('roles_id')
    url = "http://192.168.53.105:5000/v3/roles/%s" % (roles_id)
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_del = requests.delete(url, headers=headers)
    return redirect('zy405:roles')


# 获取映像的信息
def get_images(domain_token):
    url = "http://192.168.53.105:9292/v2/images"
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.get(url, headers=headers)
    # print("images: ",resp.json())
    return resp


# 获取映像列表
def images_list(request):
    domain_token = request.session.get("domain_token")
    project_token = request.session.get("v3_token")
    if not(domain_token and project_token):
        return redirect('zy405:login')

    else:
        resp = get_images(domain_token)
        if resp.status_code == 200:
            images_datas = resp.json()["images"]
            # print(images_datas)
            return render(request, 'images.html', {'images_datas': images_datas})

        else:
            return redirect('zy405:images')


# 创建映像
def cre_images(request):
    domain_token = request.session.get("domain_token")
    project_token = request.session.get("project_token")
    name = request.POST.get('name')
    container_format = request.POST.get('container_format')
    disk_format = request.POST.get('disk_format')
    description = request.POST.get('description')
    # status = request.POST.get('status')
    # protected = request.POST.get('protected')
    # disk_format = request.POST.get('disk_format')
    # size = request.POST.get('size')
    url = "http://192.168.53.105:5000/v3/images"
    data = {
        "image": {
            "owner": "71dd930094aa458aad94b74d48a3b48b",  # 项目标识
            # "domain_id": "1bd27b03b1974c81a2bf286ef8f35d0a",
            "container_format": container_format,
            "disk_format": disk_format,
            "name": name,
            # "status": "active",
            # "protected": "False",
            # "size": "13287936",
            "description": description,
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)
    return redirect('zy405:images')

#  上传映像


def upload_images(request):
    domain_token = request.session.get("domain_token")
    images_id = request.POST.get('images_id')
    url = "http://192.168.53.105:5000/v3/images/%s" % (images_id)
    data = {
        "image": {
            "path": "F:\hello-traditional_2.10-5_amd64.deb"
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    headers["Content-Type"] = "application/octet-stream"
    resp_update = requests.put(url, data=json.dumps(data), headers=headers)
    print(resp_update)
    return redirect('zy0405:images')


def upload(request):
    images_id = request.POST.get('images_id')
    object = request.FILES.get('obj')
    object_name = object.name
    url = "http://192.168.53.105:5000/v3/images/%s" % (images_id)
    with open(object_name, 'wb') as f:
        for files in object:
            f.write(files)
    data = open(object.name, 'r',)
    print(data)
    headers = {}
    headers["X-Auth-Token"] = request.session['domain_token']
    resp_update = request.PUT(url, data=json.dumps(data), headers=headers)
    print(resp_update)
    return redirect('zy0405:images')
    # return HttpResponseRedirect("/login/%s"%(count_name))

#  更新映像


def update_images(request):
    name = request.POST.get('name')
    domain_token = request.session.get("domain_token")
    images_id = request.POST.get('images_id')
    url = "http://192.168.53.105:5000/v3/images/%s" % (images_id)
    data = {
        "image": {
            "name": name
        }
    }
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_update = requests.patch(url, data=json.dumps(data), headers=headers)
    print(resp_update)
    return redirect('zy405:images')


#  删除映像
def del_images(request, images_id):
    domain_token = request.session.get("domain_token")
    # images_id = request.POST.get('images_id')
    url = "http://192.168.53.105:5000/v3/images/%s" % (images_id)
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp_del = requests.delete(url, headers=headers)
    return redirect('zy0405:images')

###############################


def get_flavors(domain_token):
    url = "http://192.168.53.105:8774/v2.1/flavors"
    headers = {}
    headers['X-Auth-Token'] = domain_token
    resp = requests.get(url, headers=headers)
    print("flavors: ", resp.json())
    # print(resp)
    return resp


# 获取用户列表
def flavors_list(request):
    domain_token = request.session.get("domain_token", None)
    v3_token = request.session.get("v3_token", None)
    if not(domain_token and v3_token):
        return redirect('zy405:login')

    else:
        resp = get_flavors(v3_token)
        if resp.status_code == 200:
            # request.session["users_list"] = resp.json()
            flavors_data = resp.json()["flavors"]
            print(flavors_data)
            return render(request, 'flavors.html', {'flavors_datas': flavors_data})
        else:
            return redirect('zy405:flavors')


def do_bytes(bytes_data):

    for i in range(len(bytes_data)):
        bytes_data[i]['bytes'] /= 128  # 单位换算kb  1kb= 1024bit = 128 bytes

        if bytes_data[i]['bytes'] < 1024:  # 不足1Mb 用kb 单位
            bytes_data[i]['bytes'] = str(
                round(bytes_data[i]['bytes'], 2)) + 'Kb'

        # 大于1mb 小于1gb 用mb单位
        elif bytes_data[i]['bytes'] >= 1024 and bytes_data[i]['bytes'] < (1024**2):
            bytes_data[i]['bytes'] /= 1024

            bytes_data[i]['bytes'] = str(
                round(bytes_data[i]['bytes'], 2)) + 'Mb'
        elif bytes_data[i]['bytes'] >= (1024**2):  # 字节 大 用gb单位
            bytes_data[i]['bytes'] /= (1024**2)

            bytes_data[i]['bytes'] = str(
                round(bytes_data[i]['bytes'], 2)) + 'Gb'
        # round(bytes_data[i]['bytes'],2)
        print(bytes_data[i]['bytes'])
    return bytes_data


bytes_data = [{'count': 1, 'bytes': 13, 'name': 'Ben'}, {'count': 0, 'bytes': 999999999, 'name': 'aaa'},
              {'count': 1, 'bytes': 133, 'name': 'Ben'}, {
                  'count': 1, 'bytes': 112333, 'name': 'Ben'},
              {'count': 1, 'bytes': 1333333, 'name': 'Ben'}, {
    'count': 1, 'bytes': 15555, 'name': 'Ben'},
]
# do_bytes(bytes_data)
obj_data = [{'hash': '184b5f1dd964e47d458361186b0d61c6', 'last_modified': '2021-11-27T13:29:25.749070',
             'bytes': '7.1Mb', 'name': 'demo1.jpg', 'content_type': 'image/jpeg'},
            {'hash': '8b4adc1ee88cc17a2aed2242ebb3fcea', 'last_modified': '2021-12-01T12:54:33.094150', 'bytes': '38.63Mb',
            'name': 'demo2.docx', 'content_type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'},
            {'hash': '9a2dd62c6a71278110aa30bfe246112b', 'last_modified': '2021-11-27T13:48:54.030640', 'bytes': '12.62Mb',
            'name': 'demo3.mp4', 'content_type': 'video/mp4'},
            {'hash': '9a887b0e398629d144f07edfb6d6e232', 'last_modified': '2021-11-17T02:54:16.664950', 'bytes': '1.04Mb',
             'name': 'tu1.jpg', 'content_type': 'image/jpeg'},
            {'hash': '9d0856b681019ae81e8ac05aee174b2c', 'last_modified': '2021-11-17T02:54:25.840100', 'bytes': '969.55Kb',
             'name': 'tu2.jpg', 'content_type': 'image/jpeg'},
            {'hash': '184b5f1dd964e47d458361186b0d61c6', 'last_modified': '2021-11-17T02:54:32.645530', 'bytes': '7.1Mb',
             'name': 'tu3.jpg', 'content_type': 'image/jpeg'}]


def do_time(obj_data):
    for i in range(len(obj_data)):
        obj_data[i]['last_modified'] = obj_data[i]['last_modified'].split(".", 1)[
            0]
        obj_data[i]['last_modified'] = obj_data[i]['last_modified'].replace(
            "T", " ")
        # round(bytes_data[i]['bytes'],2)
        print(obj_data[i]['last_modified'])
    return obj_data

# do_time(obj_data)


def get_project_id(name):
    data = {'links': {'self': 'http://192.168.53.105:5000/v3/auth/projects?format=json', 'previous': None, 'next': None}, 'projects': [{'is_domain': False, 'description': 'project-work swift', 'links': {'self': 'http://192.168.53.105:5000/v3/projects/19c7ac507b9a41a8999e77bebc11e54a'}, 'enabled': True, 'id': '19c7ac507b9a41a8999e77bebc11e54a', 'parent_id': 'f35a42e4bed84bb6aae492b7e2bc8b0f', 'domain_id': 'f35a42e4bed84bb6aae492b7e2bc8b0f', 'name': 'ceshi'}, {
        'is_domain': False, 'description': 'Admin Project', 'links': {'self': 'http://192.168.53.105:5000/v3/projects/71dd930094aa458aad94b74d48a3b48b'}, 'enabled': True, 'id': '71dd930094aa458aad94b74d48a3b48b', 'parent_id': 'f35a42e4bed84bb6aae492b7e2bc8b0f', 'domain_id': 'f35a42e4bed84bb6aae492b7e2bc8b0f', 'name': 'admin'}]}
    for i in range(len(data)):
        if name == data["projects"][i]["name"]:
            project_id = data["projects"][i]["id"]
        else:
            project_id = None
    # print(pro_id)
    return project_id

# get_project_id("ceshi")


def get_all_objects():
    data1 = [{'count': 1, 'bytes': 13, 'name': 'Ben'}, {'count': 2, 'bytes': 0, 'name': 'animals'}, {'count': 1, 'bytes': 5063414, 'name': 'bb'}, {
        'count': 3, 'bytes': 36018067, 'name': 'ggg'}, {'count': 1, 'bytes': 14, 'name': 'zy0405'}, {'count': 8, 'bytes': 44268419, 'name': 'zy1'}]
    data2 = [{'count': 1, 'bytes': 13, 'name': 'Ben'}, {'count': 2, 'bytes': 0, 'name': 'animals'}, {'count': 1, 'bytes': 5063414, 'name': 'bb'}, {
        'count': 3, 'bytes': 36018067, 'name': 'ggg'}, {'count': 1, 'bytes': 14, 'name': 'zy0405'}, {'count': 8, 'bytes': 44268419, 'name': 'zy2'}]
    data1 += data2
    print(data1)
    return data1

# get_all_objects()

def do_split():
    objlink = "AUTH_542629b3b00f4a47854f47fd084da3e0/aaaaa/demo3.mp4"
    print(objlink.split("/",1)[0])

    return None
# do_split()

import time
def do_recently_time(dt):
    timeArray = time.strptime(dt,"%Y-%m-%dT%H:%M:%S")
    timestamp = time.mktime(timeArray)
    print(timestamp)
    nowtime = time.time()
    print(nowtime)
    if (nowtime - timestamp) <= (24 * 60 * 60):
        return True
    else:
        return False


# do1_time("2023-04-12T08:44:18")

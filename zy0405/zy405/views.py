# Create your views here.
import time
import io
import json
import math
import os

import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from PIL import Image

# keystone api
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


def get_project_token(username, passwd):
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
                        "password": passwd,
                    }
                }
            },
            "scope": {
                "project": {
                    "domain": {
                        "name": "default"
                    },
                    "name": username
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

# 获取操作容器admin token


def get_admin_project_token():
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

# project
# 获取项目目录 ########################################################


def get_projects():
    # project_token = request.session.get('project_token')
    project_token = get_admin_project_token()
    # url = "http://192.168.53.105:5000/v3/auth/projects"
    url = "http://192.168.53.105:5000/v3/projects"
    headers = {"X-Auth-Token": project_token}
    param = {"format": 'json'}
    resp = requests.get(url, headers=headers, params=param)
    print(resp)
    # print(resp.json())
    # return data
    return resp

# get 某一个project


def get_projects_one():
    # project_token = request.session.get('project_token')
    project_token = get_admin_project_token()
    # url = "http://192.168.53.105:5000/v3/auth/projects"
    url = "http://192.168.53.105:5000/v3/projects/70568a2e53fb482f9fc34e850bc15b0b"
    headers = {"X-Auth-Token": project_token}
    param = {"format": 'json'}
    resp = requests.get(url, headers=headers, params=param)
    # print(resp)
    # print(resp.json())
    # return data
    return resp

# get_projects_one()
# 创建项目


def cre_project(project_name):
    # name = request.POST.get('project_name')
    project_token = get_admin_project_token()
    url = "http://192.168.53.105:5000/v3/projects"
    data = {
        "project": {
            "description": "swift user project",
            "domain_id": "f35a42e4bed84bb6aae492b7e2bc8b0f",
            "enabled": True,
            "is_domain": False,
            "name": project_name,
            "options": {}
        }
    }
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)

    return resp
# cre_project()
# 获取用户的信息


# 查看域对象
def get_domin():
    project_token = get_admin_project_token()
    url = "http://192.168.53.105:5000/v3/domains/"
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.get(url, headers=headers)
    print("users: ", resp.json())
    # print(resp)
    return resp
# get_domin()

# 用户api
# 获取用户列表


def get_users():
    project_token = get_admin_project_token()
    url = "http://192.168.53.105:5000/v3/users"
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.get(url, headers=headers)
    # print("users: ", resp.json())
    # print(resp)
    return resp
# project_token = get_admin_project_token()
# get_users()

# 获取用户id


def get_users_id(name):
    data = get_users().json()
    for i in range(len(data["users"])):
        # print(data["users"][i]["name"])
        if data["users"][i]["name"] == name:
            # print(i)  # 判断不了
            users_id = data["users"][i]["id"]
            break  # key 关键步骤。debug 半天 user——id None 就是没break
        else:
            users_id = None

    # print(users_id)
    return users_id
# get_users_id("demo3")


def users_list(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not(domain_token and project_token):
        return redirect('zy405:login')

    else:
        resp = get_users()
        if resp.status_code == 200:
            request.session["users_list"] = resp.json()
            users_data = resp.json()["users"]
            # print(users_data)
            return render(request, 'users.html', {'users_data': users_data})
        else:
            return redirect('zy405:users')

# 创建用户


def cre_users(name, password, email, project_id):
    project_token = get_admin_project_token()
    # print(project_token)
    # project_token = request.session.get("project_token")
    # name = request.POST.get('name')
    # description = request.POST.get('description')
    # email = request.POST.get('email')
    url = "http://192.168.53.105:5000/v3/users"
    data = {
        "user": {
            "name": name,
            "enabled": True,
            "domain_id": "f35a42e4bed84bb6aae492b7e2bc8b0f",
            "description": "swift user",
            "email": email,
            "password": password,
            "default_project_id": project_id
        }
    }
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)
    return resp
# cre_users("demo3","1234","123@qq.com","9a377e477e3e4e8f8a60335374855e03")
#  更新用户


def update_users(request, name, description, user_id, email):
    project_token = request.session.get("project_token")
    # name = request.POST.get('name')
    # description = request.POST.get('description')
    # users_id = request.POST.get('user_id')
    # email = request.POST.get('email')
    # print(email)
    url = "http://192.168.53.105:5000/v3/users/%s" % (user_id)
    data = {
        "user": {
            "description": description,
            "name": name,
            "email": email,
        }
    }
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.patch(url, data=json.dumps(data), headers=headers)
    print(resp)
    return resp

# 修改密码


def change_users_password(request, user_id, passwd, new_passwd):
    # project_token = get_admin_project_token()
    project_token = request.session.get("project_token")
    # name = request.POST.get('name')
    # description = request.POST.get('description')
    # users_id = request.POST.get('user_id')
    # email = request.POST.get('email')
    # print(email)
    url = "http://192.168.53.105:5000/v3/users/%s/password" % (user_id)
    data = {
        "user": {
            "password": new_passwd,
            "original_password": passwd
        }
    }
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.post(url, data=json.dumps(data), headers=headers)
    print(resp)
    return resp


# 角色 api
# 获取 角色
def get_roles():
    project_token = get_admin_project_token()
    url = "http://192.168.53.105:5000/v3/roles"
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.get(url, headers=headers)
    print("roles: ", resp.json())
    print(resp)
    return resp
# project_token = get_admin_project_token()
# get_roles()
# 获取角色的id


def get_roles_id():
    data = get_roles().json()
    for i in range(len(data["roles"])):
        print(data["roles"][i]["name"])
        if data["roles"][i]["name"] == "user":
            print(i)  # 判断不了
            roles_id = data["roles"][i]["id"]
            break  # key 关键步骤。debug 半天 project——id None 就是没break
        else:
            roles_id = None

    print(roles_id)
    return roles_id
# get_roles_id()
# Assigns a role to a user on a project.
# 注册功能的关键！！！


def assign_user_project(project_id, user_id, roles_id):

    project_token = get_admin_project_token()
    url = "http://192.168.53.105:5000/v3/projects/%s/users/%s/roles/%s" % (
        project_id, user_id, roles_id)
    headers = {}
    headers['X-Auth-Token'] = project_token
    resp = requests.put(url, headers=headers)
    # print("roles: ", resp.json())
    print(resp)
    return resp

# assign_user_project("9a377e477e3e4e8f8a60335374855e03","ec2edb9a232a443b834ad0b49612a2ba","162b6562f063401e97dbd6f94c1e05b8")

# 容器模块 API
# 获取 容器


def get_swift_counters(request):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/?format=json" % (project_id)
    headers = {}
    # print("conter_datas")
    headers["X-Auth-Token"] = request.session.get('project_token')
    resp = requests.get(url, headers=headers)
    # print(resp)
    # if resp.content:
    # conter_datas = resp.json()
    # print(resp.json())
    # return render(request, 'homepage.html', {'conter_datas': conter_datas})
    return resp

# 新建容器


def put_counter(request, conname, meta_name):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s?format=json" % (project_id,
                                                                    conname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    headers["X-Container-Meta-InspectedBy"] = meta_name
    resp = requests.put(url, headers=headers)
    return resp

# 删除容器


def delete_counter(request, conname):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s?format=json" % (project_id,
                                                                    conname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    resp = requests.delete(url, headers=headers)
    return resp

# 对象 api
# 获取 容器里的文件


def get_swift_objects(request, conname):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s?format=json" % (
        project_id, conname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    resp = requests.get(url, headers=headers)
    # obj_datas = resp.json()
    # return render(request, 'homepage.html', {'obj_datas': obj_datas})
    return resp
    # return obj_datas

# 查看对象


def get_swift_object(request, conname, objname):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s/%s?format=json" % (project_id,
                                                                       conname, objname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    resp = requests.get(url, headers=headers)
    return resp

# 上传对象文件


def put_object(request, conname, objname, content, content_type):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s/%s?format=json" % (project_id,
                                                                       conname, objname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    headers["Content-Type"] = content_type
    resp = requests.put(url, headers=headers, data=content)
    return resp

#  下载对象文件


def download_object(request, conname, objname):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s/%s?format=json" % (project_id,
                                                                       conname, objname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    resp = requests.get(url, headers=headers)
    return resp

# 复制对象


def copy_object(project_token, project_id, conname, objname, copy_conname, copy_objname):
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s/%s?format=json" % (project_id,
                                                                       conname, objname)
    headers = {}
    headers["X-Auth-Token"] = project_token
    headers["Content-Length"] = "0"

    # 被copy 的对象以及容器名
    headers["X-Copy-From"] = "%s/%s" % (copy_conname, copy_objname)
    resp = requests.put(url, headers=headers)
    return resp

    # curl -i http://192.168.53.105:8080/v1/AUTH_71dd930094aa458aad94b74d48a3b48b/bb/demo9.txt
    # -X PUT
    # -H "X-Auth-Token: gAAAAABkNAYAO41WUWNkv5EjeTebQ2mvRv4BPb8awGPZIONq5U6vhT58WN2IOwGF2kVDqrxjaIj8wyJ83yfuUpfuKCBHyzFlIHF6q0rTvhLf0Oa77XYZGi4UXJEh3dve_xcQPLEifKBwxywHiy2L9oghxqglG12X6hIS0xEUOyfLwHq1BpdTaIk"
    # -H "X-Copy-From: Ben/demo8.txt"
    # -H "Content-Length: 0"
    # -H "X-Copied-From-Account: AUTH_542629b3b00f4a47854f47fd084da3e0"
    # headers["Destination"] = "bb/demo3.jpg"

# 获取其他用户分享的文件


def get_share_object(project_token, project_id, conname, objname, share_project_id, share_conname, share_objname):
    print(project_id, conname, objname,
          share_project_id, share_conname, share_objname)
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s/%s?format=json" % (project_id,
                                                                       conname, objname)
    # url = "http://192.168.53.105:8080/v1/AUTH_542629b3b00f4a47854f47fd084da3e0/bb/demo8.txt?format=json"
    headers = {}
    # headers["X-Auth-Token"] = "gAAAAABkNV6kBkkj8r4wNcxqLzZy_8Qeei-mXLz3vPeKH7Oh4PE4ZypAX6VdDiX-NDAIl0GdjxEHRA72ebhuLe5QmLmZqFJw2RcQIgxwebWuE8FyxTr5UwG_den0Tx1I6DuyYTT2vFKz96bGzP5xwhCLCl93lJN_UeKn2N1yk5-xYmgp3ufOEXI"
    headers["X-Auth-Token"] = project_token
    headers["Content-Length"] = "0"
    # 被copy 的对象以及容器名
    headers["X-Copy-From"] = "%s/%s" % (share_conname, share_objname)
    # 被copy 对象的project地址
    headers["X-Copied-From-Account"] = "%s" % (share_project_id)
    # headers["X-Copy-From-Account"] = "AUTH_70568a2e53fb482f9fc34e850bc15b0b" # 被copy 对象的project地址
    # headers["X-Copy-From"] = "Ben/demo8.txt" # 被copy 的对象以及容器名

    resp = requests.put(url, headers=headers)
    print(resp)
    # data = resp.json()
    # print(data)
    return resp

# 删除文件


def delete_object(request, conname, objname):
    project_id = request.session.get('project_id')
    url = "http://192.168.53.105:8080/v1/AUTH_%s/%s/%s?format=json" % (project_id,
                                                                       conname, objname)
    headers = {}
    headers["X-Auth-Token"] = request.session.get('project_token')
    resp = requests.delete(url, headers=headers)
    return resp


######################
# 获取 project_id——> auth_id
def get_project_id(name):
    data = get_projects().json()
    # print(len(data["projects"]))
    # print(data)
    # print(name)
    # print(data["projects"][5]["id"])
    # print(data["projects"][5]["name"] == name)
    for i in range(len(data["projects"])):
        print(data["projects"][i]["name"])
        if data["projects"][i]["name"] == name:
            # print(i)  # 判断不了
            project_id = data["projects"][i]["id"]
            break  # key 关键步骤。debug 半天 project——id None 就是没break
        else:
            project_id = None

    print(project_id)
    return project_id

## 登陆模块 ##########


def login(request):
    return render(request, "login.html")


def loginCheck(request):
    uname = request.POST.get('username')
    passwd = request.POST.get('passwd')
    # print(uname,passwd)
    result = get_domain_token(uname, passwd)
    # print(result)
    domain_token = result.headers.get("X-Subject-Token")
    project_token = get_project_token(uname, passwd)
    # print(project_token)
    # print(domain_token)
    if (result.status_code == 201 or result.status_code == 200):
        request.session["user"] = uname
        request.session['domain_token'] = domain_token
        request.session['project_token'] = project_token
        project_id = get_project_id(uname)
        # print(project_id)
        request.session['project_id'] = project_id
        # return render(request, 'index.html')
        return redirect("/swift/index")
    else:
        return redirect("/swift/login")


def loginout(request):
    request.session.flush()
    return redirect('/swift/login')

# 注册模块


def sign_up(request):
    return render(request, "signup.html")


def sign_up_action(request):
    uname = request.POST.get('username')
    passwd = request.POST.get('passwd')
    email = request.POST.get('email')
    print(uname)
    if uname == "" and passwd == "" and email == "":
        info = "input error"
        return JsonResponse({"info": info})
    else:
        users_data = get_users().json()  # 检索 是否重名 用户名重复则报错
        for i in range(len(users_data["users"])):
            # print(users_data["users"][i]["name"])
            if uname == users_data["users"][i]["name"]:
                info = "name error"
                return JsonResponse({"info": info})
        resp = cre_project(uname) # 创建Project
        # print(resp)
        if resp.status_code == 201:
            # project_token = get_admin_project_token()
            project_id = get_project_id(uname) #获取Projectid
            # print(project_id)
            result = cre_users(uname, passwd, email, project_id) #创建用户
            if result.status_code == 201:
                roles_id = get_roles_id() #获取Roleid表
                user_id = get_users_id(uname)#获取注册用户的id
                # KEY：分配User进入Project
                rp = assign_user_project(project_id, user_id, roles_id)
                if rp.status_code == 204:
                    info = "sign up ok"
                    return redirect('/swift/login')
                else:
                    info = "assign definte"
                    return JsonResponse({"info": info})
        else:
            info = "create proejct error"
            return JsonResponse({"info": info})


# sign_up()
# 修改密码
def change_password(request):
    return render(request, "change_pwd.html")


def change_password_action(request):
    original_password = request.POST.get('original_password')
    newpasswd = request.POST.get('passwd1')
    print(original_password, newpasswd)
    if original_password == "" and newpasswd == "":
        info = "input error"
        return JsonResponse({"info": info})
    else:
        uname = request.session.get("user")
        users_id = get_users_id(uname)
        print(users_id)

        resp = change_users_password(
            request, users_id, original_password, newpasswd)
        print(resp)
        if resp.status_code == 204:
            # qingchu session
            request.session.flush()
            return redirect("/swift/login")
        else:
            info = " change error"
            return JsonResponse({"info": info})


# 跳转主页


def index(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    uname = request.session.get("user", None)
    print(project_token)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        resp = get_swift_counters(request)
        print(resp)
        if resp.status_code == 200:
            counter_datas = resp.json()
            counter_datas = do_bytes(counter_datas)
            # request.session["list_containers"] = resp.json()
            # return render(request, 'zgh0381/container_list.html')
            return render(request, 'counter.html', {'counter_datas': counter_datas, "uname": uname})
        else:
            return redirect('/swift/login')


# 容器 api 调用
# 获取容器并跳转网页
def get_counters_web(request):
    counter_datas = get_swift_counters(request)
    counter_datas = counter_datas.json()
    print(counter_datas)
    do_bytes(counter_datas)
    return render(request, 'counter.html', {'counter_datas': counter_datas})


# 创建容器
def add_counter(request):
    conname = request.POST.get("conname")
    meta_name = request.POST.get("meta")
    # print(conname)
    resp = put_counter(request, conname, meta_name)
    # counter_datas = get_swift_counters()
    if resp.status_code == 201:
        return redirect("/swift/getcon/")
    else:
        return redirect("/swift/getcon/")
        # return render(request, 'counter.html')


# 删除容器
def del_counter(request, conname):
    # conname = request.POST.get("conname")
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        resp = delete_counter(request, conname)
        if resp.status_code == 204:  # 删除成功
            return redirect("/swift/getcon/")
        elif resp.status_code == 404:  # 没有改容器
            return redirect("/swift/getcon/")
        elif resp.status_code == 409:  # 容器不为空
            return redirect("/swift/getcon/")
        # 需要改进  放回 状态码 错误信息

##############
# 获取容器中对象并跳转网页


def get_objects_web(request, conname):
    object_datas = get_swift_objects(request, conname)
    counter_datas = get_swift_counters(request)
    counter_datas = counter_datas.json()
    object_datas = object_datas.json()
    print(object_datas)
    project_id = request.session.get("project_id")
    do_data(object_datas)  # 对 json 数据中 一些值进行处理
    return render(request, 'filetable.html',
                  {'obj_datas': object_datas, 
                  'counter_datas': counter_datas, 
                  'conname': conname, 
                  'project_id': project_id})

# 获取 所有 对象


def get_all_objects(request):
    # conname = reques
    counter_datas = get_swift_counters(request)
    counter_datas = counter_datas.json()
    # print(counter_datas)
    object_datas = []
    for i in range(len(counter_datas)):
        couname = counter_datas[i]["name"]
        object_data = get_swift_objects(request, couname).json()
        object_datas += object_data
    # print(object_datas)
    # do_data(object_datas)
    return object_datas


def get_all_objects_web(request):
    # conname = request.POST.get("conname")
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        object_datas = get_all_objects(request)
        do_data(object_datas)
        return render(request, 'allfiles.html',
                      {'obj_datas': object_datas})

# 获取 指定类型对象
# 获取指定文件名


def get_search_objects(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        obj_data = get_all_objects(request)#获取所有对象
        # print(obj_data)
        name = request.POST.get("objname")
        object_datas = []
        for i in range(len(obj_data)):
            if name in obj_data[i]['name']:
                object_datas.append(obj_data[i])
                # print(obj_data[i])
                # print(object_datas)
        do_data(object_datas)
        return render(request, 'onefiles.html',
                      {'obj_datas': object_datas})
# 获取 图片


def get_img_objects(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        obj_data = get_all_objects(request)
        # print(obj_data)
        object_datas = []
        for i in range(len(obj_data)):
            if obj_data[i]['content_type'] == "image/jpeg":
                object_datas.append(obj_data[i])
                # print(obj_data[i])
                # print(object_datas)
        do_data(object_datas)
        return render(request, 'onefiles.html',
                      {'obj_datas': object_datas})
# 获取 文档


def get_doc_objects(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        obj_data = get_all_objects(request)
        # print(obj_data)
        object_datas = []
        for i in range(len(obj_data)):
            if "document" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
                # print(obj_data[i])
                # print(object_datas)
        do_data(object_datas)
        return render(request, 'onefiles.html',
                      {'obj_datas': object_datas})
# 获取 视频


def get_video_objects(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        obj_data = get_all_objects(request)
        # print(obj_data)
        object_datas = []
        for i in range(len(obj_data)):
            if "mp4" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
            elif "png" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])

                # print(obj_data[i])
                # print(object_datas)
        do_data(object_datas)
        return render(request, 'onefiles.html',
                      {'obj_datas': object_datas})
# 获取 其他


def get_other_objects(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        obj_data = get_all_objects(request)
        # print(obj_data)
        object_datas = []
        for i in range(len(obj_data)):
            if "mpeg" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
            elif "pdf" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
            elif "png" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
            elif "rar" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
            elif "octet-stream" in obj_data[i]['content_type']:
                object_datas.append(obj_data[i])
                # print(obj_data[i])
                # print(object_datas)
        do_data(object_datas)
        return render(request, 'onefiles.html',
                      {'obj_datas': object_datas})


# 获取 最近使用的对象


def get_recently_objects(request):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    # print(conname)
    else:
        obj_data = get_all_objects(request)
        # print(obj_data)
        object_datas = []
        for i in range(len(obj_data)):
            last_modified = obj_data[i]['last_modified']
            modified_time = last_modified.split(".")[0]

            if do_recently_time(modified_time):  # 判断时间是否为最近一天
                object_datas.append(obj_data[i])

                # print(obj_data[i])
                # print(object_datas)
        do_data(object_datas)
        return render(request, 'onefiles.html',
                      {'obj_datas': object_datas})


# 对象预览 需要改进


def get_object(request, conname, objname):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        resp = get_swift_object(request, conname, objname)
        if resp.status_code == 200:
            object_content = resp.text
            return JsonResponse({"object-content": object_content})
        elif resp.status_code == 404 or resp.status_code == 416:
            info = "open error"
            return JsonResponse({"info": info})


# 对象上传

def add_object(request, conname):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)

    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        filename = request.POST.get("upload_file")
        suffix = filename[filename.rfind('.') + 1:]
        Base_path = os.path.dirname(os.path.dirname(__file__))
        file_path = Base_path + "\\zy0405\\static\\upload\\"
        # print(file_path)
        # print(suffix)
        if suffix == 'txt':
            with open(file_path + filename, 'rb') as local:
                obj_content = local.read()
            content_type = "text/plain"
            rep = put_object(request, conname, filename,
                             obj_content, content_type)
            print(rep)
            if rep.status_code == 201:
                # print(filename)
                return get_objects_web(request, conname)
        elif suffix == 'png':
            with open(file_path + filename, 'rb') as local:
                obj_data = local.read()
            content_type = "image/png"
            rep = put_object(request, conname, filename,
                             obj_data, content_type)
            if rep.status_code == 201:
                # img = 'png.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        elif suffix == 'jpg':
            with open(file_path + filename, 'rb') as local:
                obj_data = local.read()
            content_type = "image/png"
            rep = put_object(request, conname, filename,
                             obj_data, content_type)
            if rep.status_code == 201:
                # img = 'png.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        elif suffix == 'docx':
            with open(file_path + filename, 'rb') as local:
                obj_data = local.read()
            content_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            rep = put_object(request, conname, filename,
                             obj_data, content_type)
            if rep.status_code == 201:
                # img = 'docx.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        elif suffix == 'pdf':
            with open(file_path + filename, 'rb') as local:
                obj_data = local.read()
            content_type = "application/pdf"
            rep = put_object(request, conname, filename,
                             obj_data, content_type)
            if rep.status_code == 201:
                # img = 'pdf.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        elif suffix == 'mp4':
            with open(file_path + filename, 'rb') as local:
                obj_data = local.read()
            content_type = "video/mp4"
            rep = put_object(request, conname, filename,
                             obj_data, content_type)
            if rep.status_code == 201:
                # img = 'mp4.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        elif suffix == 'mp3':
            with open(file_path + filename, 'rb') as local:
                obj_data = local.read()
            content_type = "audio/mpeg"
            rep = put_object(request, conname, filename,
                             obj_data, content_type)
            if rep.status_code == 201:
                # img = 'mp3.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        elif suffix == 'rar':
            with open(file_path + filename, 'rb') as local:
                obj_content = local.read()
            content_type = "application/rar"
            rep = put_object(request, conname, filename,
                             obj_content, content_type)
            if rep.status_code == 201:
                # img = 'jpg.png'
                # request.session['img'] = img
                return get_objects_web(request, conname)
        else:
            return get_objects_web(request, conname)


# 对象下载


def down_object(request, conname, objname):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    # print(conname, objname)
    suffix = objname[objname.rfind('.') + 1:]
    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        r = HttpResponse(content_type='application/octet-stream')
        r['Content-Disposition'] = 'attachment;filename="{0}"'.format(objname)
        resp = download_object(request, conname, objname)
        if resp.status_code == 200:
            if suffix == 'txt':
                r.write(str(resp.text))
            elif suffix == 'jpg':
                byte_stream = io.BytesIO(resp.content)
                roiImg = Image.open(byte_stream)
                imgByteArr = io.BytesIO()
                roiImg.save(imgByteArr, format='jpeg')
                imgByteArr = imgByteArr.getvalue()
                r.write(imgByteArr)
            elif suffix == 'png':
                byte_stream = io.BytesIO(resp.content)
                roiImg = Image.open(byte_stream)
                imgByteArr = io.BytesIO()
                roiImg.save(imgByteArr, format='png')
                imgByteArr = imgByteArr.getvalue()
                r.write(imgByteArr)
            elif suffix == 'docx':
                r.write(resp.content)
            elif suffix == 'pdf':
                r.write(resp.content)
            elif suffix == 'mp4':
                r.write(resp.content)
            else:
                r.write(resp.content)

        return r


# 获得分享的文件

def get_share_object_action(request, conname):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    # print(project_token)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        objlink = request.POST.get("get_share_object")
        if objlink == "":
            info = "link error"
            return JsonResponse({"info": info})
        else:
            # link AUTH_542629b3b00f4a47854f47fd084da3e0/aaaaa/demo3.mp4
            # AUTH_542629b3b00f4a47854f47fd084da3e0
            share_project_id = objlink.split('/')[0]
            share_conname = objlink.split("/")[1]  # aaaaa
            share_objname = objlink.split("/")[2]  # demo3.mp4
            # print(share_project_id,share_conname,share_objname)
            project_id = request.session.get("project_id")
            # conname = request.POST.get("conname")
            objname = request.POST.get("objname")
            # print(conname,objname)
            resp = get_share_object(project_token, project_id, conname,
                                    objname, share_project_id, share_conname, share_objname)
            if resp.status_code == 201:
                return get_objects_web(request, conname)
            else:
                info = "save error"
                # return JsonResponse({"info": info})
                return get_objects_web(request, conname)
# 复制文件

def copy_object_action(request, conname):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    # print(project_token)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        # link AUTH_542629b3b00f4a47854f47fd084da3e0/aaaaa/demo3.mp4
        # AUTH_542629b3b00f4a47854f47fd084da3e0
        # print(share_project_id,share_conname,share_objname)
        project_id = request.session.get("project_id")
        copied_conname = request.POST.get("copied_conname")
        objname = request.POST.get("copied_objname")
        # print(conname,copied_conname,objname)
        resp = copy_object(project_token, project_id, copied_conname,
                                objname, conname, objname)
        print(resp)
        if resp.status_code == 201:
            return get_objects_web(request, conname)
        else:
            info = "save error"
            return JsonResponse({"info": info})


# 对象删除


def del_object(request, conname, objname):
    domain_token = request.session.get("domain_token", None)
    project_token = request.session.get("project_token", None)
    if not (domain_token and project_token):
        return redirect('/swift/login')
    else:
        resp = delete_object(request, conname, objname)
        if resp.status_code == 204:
            return get_objects_web(request, conname)
####################################################

# 中间件
# 数据处理部分
# 大方法调用小方法


def do_data(data):
    do_bytes(data)
    do_time(data)
    do_type(data)
    return data
# 文件大小单位换算


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
        # print(bytes_data[i]['bytes'])
    return bytes_data

# 修改时间格式


def do_time(obj_data):
    for i in range(len(obj_data)):
        obj_data[i]['last_modified'] = obj_data[i]['last_modified'].split(".", 1)[
            0]
        obj_data[i]['last_modified'] = obj_data[i]['last_modified'].replace(
            "T", " ")
        # round(bytes_data[i]['bytes'],2)
        # print(obj_data[i]['last_modified'])
    return obj_data

# 修改文件类型


def do_type(obj_data):
    for i in range(len(obj_data)):
        if obj_data[i]['content_type'] == "image/jpeg":
            obj_data[i]['content_type'] = "jpeg"
        elif "document" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "document"
        elif "mpeg" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "mp3"
        elif "mp4" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "mp4"
        elif "text" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "text"
        elif "pdf" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "pdf"
        elif "png" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "png"
        elif "rar" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "rar"
        elif "octet-stream" in obj_data[i]['content_type']:
            obj_data[i]['content_type'] = "octet-stream"

    # round(bytes_data[i]['bytes'],2)
    # print(obj_data[i]['last_modified'])
    return obj_data

# 删除 session


def delete_session(request):
    request.session
    return None

# 判断文件 时间是否一天内


def do_recently_time(dt):
    timeArray = time.strptime(dt, "%Y-%m-%dT%H:%M:%S")
    timestamp = time.mktime(timeArray)
    print(timestamp)
    nowtime = time.time()
    print(nowtime)
    if (nowtime - timestamp) <= (24 * 60 * 60):
        return True
    else:
        return False

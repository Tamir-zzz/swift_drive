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
# token = get_v3_token
def get_info():
    v3_token = get_v3_token()
    print(v3_token)
    # damian_token = 'gAAAAABihFiJ5WczVfk0R3f9k0F2zDJBACcrO0R-_e2bnyYt9JK_6rBJiqlVTNdJx4TkP2t_1Ay4d6-rpTlmFVGXCWFrF0Ya7aok4VFBiE3760aSPu52l_9xK7jEfp8jj937CNbTRmUCKl8-cLgu4bGIeWm6BjPA-RQF0kQOtUY-R4UMfn_xDUo'
    url = "http://192.168.53.105:5000/v1/"
    headers = {"X-Auth-Token": v3_token}
    param = {"format": 'json'}
    resp = requests.get(url, headers=headers, params=param)
    data = resp.json()
    print(data)
    # print(type(data))
    return data
get_info()

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

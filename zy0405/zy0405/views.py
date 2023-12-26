# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render_to_response,RequestContext
import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect


def initLogin(request):
    # projects_datas = get_projects()
    # return render(request, '/swift/login/')
    return redirect('zy405:login')

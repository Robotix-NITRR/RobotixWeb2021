from django.shortcuts import render,redirect
from extras.models import web, app
import datetime
import time
def index(request):
    return render(request,'index.html')


def webteam(request):
    webteam_obj = web.objects.all()
    appteam_obj = app.objects.all()
    dict = {'web' : webteam_obj , 'app' : appteam_obj}
    return render(request,'web-team.html', context=dict)


def robothondetail(request):
    return render(request,'robothon.html')


def roboexpodetail(request):
    return render(request,'roboexpo.html')

def robofestdetail(request):
    return render(request,'robofest.html')

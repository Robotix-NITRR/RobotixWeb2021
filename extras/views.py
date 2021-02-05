from django.shortcuts import render
from .models import FYI,DIY
from . models import sponsors as Spons

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import DIYSerializer,FYISerializer,SponsorSerializer
# Create your views here

@api_view()
def diy_api(request):
    obj_diy = DIY.objects.all()
    serializer = DIYSerializer(obj_diy,many=True)
    dict = {'diy':serializer.data}
    # return render(request,'diy.html',context=dict)
    return Response(dict)

@api_view()
def fyi_api(request):
    obj_fyi = FYI.objects.all()
    serializer = FYISerializer(obj_fyi,many=True)
    dict = {'fyi':serializer.data}
    # return render(request,'fyi.html',context=dict)
    return Response(dict)


def diy(request):
    obj_diy = DIY.objects.all()
    # serializer = DIYSerializer(obj_diy,many=True)
    dict = {'diy':obj_diy}
    return render(request,'diy.html',context=dict)
    # return Response(dict)


def fyi(request):
    obj_fyi = FYI.objects.all()
    # serializer = FYISerializer(obj_fyi,many=True)
    dict = {'fyi':obj_fyi}
    return render(request,'fyi.html',context=dict)
    # return Response(dict)

def sponsors(request):
    all_sponsors = Spons.objects.all()
    return render(request,'sponsors.html',{'all_sponsors':all_sponsors})

class sponsors_api(viewsets.ModelViewSet):
    queryset = Spons.objects.all()
    serializer_class = SponsorSerializer

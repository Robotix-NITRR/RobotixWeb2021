from django.shortcuts import render
from .models import Alumni
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlumniSerializer
# Create your views here.


@api_view()
def alumni_api(request):
    obj_alumni = Alumni.objects.all()
    # obj_year = []
    # for i in obj_alumni:obj_year.append(i.year)
    # new_lst = list(set(obj_year))
    # new_lst.sort()
    serializer = AlumniSerializer(obj_alumni,many=True)
    dict = {'alum':serializer.data}
    # return render(request,'alumni.html',context=dict)
    return Response(dict)

@api_view()
def alumni(request):
    obj_alumni = Alumni.objects.all()
    obj_year = []
    for i in obj_alumni:obj_year.append(i.year)
    new_lst = list(set(obj_year))
    new_lst.sort()
    # serializer = AlumniSerializer(obj_alumni,many=True)
    dict = {'alum':new_lst}
    return render(request,'alumni.html',context=dict)
    # return Response(dict)

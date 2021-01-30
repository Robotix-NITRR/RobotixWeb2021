from django.shortcuts import render
from .models import Convenor,Coordinator,HeadCoordinator,Manager
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConvenorSerializer,CoordinatorSerializer,ManagerSerializer
# Create your views here.
@api_view()
def about_api(request):
    obj_conv = Convenor.objects.all()
    # obj_head = HeadCoordinator.objects.all()
    obj_manager = Manager.objects.all()
    obj_Cord = Coordinator.objects.all()
    # dict = {'Convenor':obj_conv, 'Head':obj_head, 'Manager':obj_manager,'Cord':obj_Cord}
    # return render(request,'aboutus.html',context=dict)
    serializer1 = ConvenorSerializer(obj_conv , many=True)
    serializer2 = CoordinatorSerializer(obj_Cord, many=True)
    serializer3 = ManagerSerializer(obj_manager,many=True)
    dict = {'Convenor':serializer1.data , 'Coordinator':serializer2.data,'Manager':serializer3.data}
    return Response(dict)

def about(request):
    obj_conv = Convenor.objects.all()
    obj_head = HeadCoordinator.objects.all()
    obj_manager = Manager.objects.all()
    obj_Cord = Coordinator.objects.all()
    dict = {'Convenor':obj_conv, 'Manager':obj_manager,'Cord':obj_Cord,'Recruits':obj_head}
    return render(request,'aboutus.html',context=dict)
    # serializer1 = ConvenorSerializer(obj_conv , many=True)
    # serializer2 = CoordinatorSerializer(obj_Cord, many=True)
    # serializer3 = ManagerSerializer(obj_manager,many=True)
    # dict = {'Convenor':serializer1.data , 'Coordinator':serializer2.data,'Manager':serializer3.data}
    # return Response(dict)

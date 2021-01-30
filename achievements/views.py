from django.shortcuts import render
from .models import Achievements
from rest_framework.decorators import api_view
from .serializers import AchievementSerializer
from rest_framework.response import Response
# Create your views here.

@api_view()
def achievement_api(request):
    obj_achievements = Achievements.objects.all()
    serializer = AchievementSerializer(obj_achievements,many=True)
    dict = {'achievement':serializer.data}
    return Response(dict)


def achievement(request):
    obj_achievements = Achievements.objects.all()
    # serializer = AchievementSerializer(obj_achievements,many=True)
    dict = {'achievement':obj_achievements}
    # return Response(dict)
    return render(request,'achievements.html',context=dict)

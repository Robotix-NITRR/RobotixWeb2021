from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import recruitment,Timer
# import datetime
import time
from django.utils import timezone
# Create your views here.
def recruitment_view(request):
    timer_obj = Timer.objects.all()
    timer_obj.reverse()
    # y = datetime.datetime(2019, 10, 16, 18, 6, 0)
    x = timer_obj[0].start
    y = timer_obj[0].stop
    # print (y)
    while True:

        x1 = timezone.now()
        # print(x)
        # x2=datetime.datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)
        # print(x1)
        time.sleep(1)
        if x<x1<y:
            if request.method == "POST":
                if (request.POST['name'] and
                request.POST['email'] and
                request.POST['phone'] and
                request.POST['whatsapp'] and
                request.POST['branch'] and
                request.POST['sem'] and
                request.POST['domain'] and
                request.POST['intro'] and
                request.POST['other_club_committee'] and
                request.POST['strength_weakness'] and
                request.POST['work'] and
                request.POST['why_robotix'] and
                request.POST['improvements_suggesions'] and
                request.POST['residence'] and
                request.POST['likert1'] and
                request.POST['likert1reason'] and
                request.POST['likert2'] and
                request.POST['likert2reason'] and
                request.POST['likert3'] and
                request.POST['likert3reason']) :
                    obj_contact = recruitment()
                    # print(request.POST.getlist('domain'))
                    obj_contact.name = request.POST['name']
                    obj_contact.email = request.POST['email']
                    obj_contact.phone = request.POST['phone']
                    obj_contact.whatsapp = request.POST['whatsapp']
                    obj_contact.branch = request.POST['branch']
                    obj_contact.semester = request.POST['sem']
                    obj_contact.domain = ','.join(request.POST.getlist('domain'))
                    obj_contact.intro = request.POST['intro']
                    obj_contact.other_club_committee = request.POST['other_club_committee']
                    obj_contact.strength_weakness = request.POST['strength_weakness']
                    obj_contact.work = request.POST['work']
                    obj_contact.why_robotix = request.POST['why_robotix']
                    obj_contact.improvements_suggesions = request.POST['improvements_suggesions']
                    obj_contact.residence = request.POST['residence']
                    obj_contact.priority = request.POST['likert1']
                    obj_contact.priority_reason = request.POST['likert1reason']
                    obj_contact.task_completion = request.POST['likert2']
                    obj_contact.task_completion_reason = request.POST['likert2reason']
                    obj_contact.intention = request.POST['likert3']
                    obj_contact.intention_reason = request.POST['likert3reason']

                    # obj_contact.tshirtcombo = request.POST['combo']
                    # obj_contact.mode_payment = request.POST['payment']
                    # obj_contact.transaction = request.POST['tranc']
                    obj_contact.save()
                    return HttpResponse("Your form was Submitted!")
                    time.sleep(3)
                    return redirect('/')
            else:
                return render(request,'recruitment-page.html')
        else:
            return redirect('/404.html')
            break

    # return render(request,'recruitment.html')


# def form(request):
#     y = datetime.datetime(2019, 10, 14, 16, 40, 0)
#     while True:
#         x = datetime.datetime.now()
#         x1=datetime.datetime(x.year,x.month,x.day,x.hour,x.minute,x.second)
#         time.sleep(1)
#         if x1<y:
#             return render(request,'form.html')
#         else:
#             return redirect('index')
#             break

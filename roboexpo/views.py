from django.shortcuts import render, get_object_or_404,redirect
from django.core.mail import send_mail
from .models import Roboexpo
from users.models import UserProfile
from django.conf import settings
from django.contrib.auth.decorators import login_required
from roboPortal.models import portalUser
# Create your views here.

def checked(name):
    r = Roboexpo.objects.all()
    for i in r:
        if name == i.team_name:
            return False
    return True

def check_user_acc(id):
    try:
        user = get_object_or_404(UserProfile, email=id)
        return True
    except:
        return False

def mail_sender(sel,id):
    r = Roboexpo.objects.get(id=id)
    if sel:
        subject = 'You have been selected for RoboExpo'
        msg = "Greetings from Robotix Club NITRR. Congratulations! Your team has been selected for ROBOEXPO 2020. Be there to present your project to the judges and the audience which will bring you closer to winning the competition."
    else:
        subject = 'You have not been selected for RoboExpo'
        msg = 'Greetings from ROBOTiX CLUB NITRR. We regret to inform you that your team was not selected for the further rounds of ROBOEXPO 2020. We expect your participation again next year. Till then Keep building.'
    send_mail(
        subject=subject,
        message=msg,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[i.email for i in r.team_mates.all()]+[r.email],
        fail_silently=True,
    )
    r.mail_delivered = True
    r.save()


@login_required
def expo(request):
    if request.user.portal.is_complete:
        if 'expo-register' in request.POST:
            if request.POST['team_name'] and request.POST['email'] and request.POST['team_mates'] and request.FILES['myfile']:
                team_name = request.POST['team_name']
                email = request.POST['email']
                team_mates = [mate.strip() for mate in request.POST['team_mates'].split(',')]
                file = request.FILES['myfile']
                if checked(team_name):
                    reg = Roboexpo(team_name=team_name)
                    reg.abstract = file
                    reg.save()
                    if check_user_acc(email):
                        reg.email = email
                        for i in team_mates:
                            if check_user_acc(i):
                                reg.team_mates.add(UserProfile.objects.get(email=i))
                            else:
                                reg.delete()
                                # print(f'{i} of your team is not registered!')
                                return render(request, 'roboexpo-registration.html', {
                                    'r': Roboexpo.objects.all(),
                                    'error': f'{i} of your team is not registered!'
                                })
                        reg.team_mates.add(UserProfile.objects.get(email=email))
                        reg.save()
                    else:
                        reg.delete()
                        # print(f'{i} of your team is not registered!')
                        return render(request, 'roboexpo-registration.html', {
                                    'r': Roboexpo.objects.all(),
                                    'error': f'{email} You are not registered!'
                                })
                else:
                    # print(f'{i} of your team is not registered!')
                    return render(request, 'roboexpo-registration.html', {
                                    'r': Roboexpo.objects.all(),
                                    'error': f'Team name: {team_name} already exists!'
                                    })
                return redirect('/accounts/account')
    else:
        if 'complete' in request.POST:
            portal = portalUser.objects.get(user = request.user)
            college = request.POST['college']
            branch = request.POST['branch']
            semester = request.POST['semester']
            # portal.description = description
            # portal.resume = resume
            portal.college = college
            portal.branch = branch
            portal.semester = semester
            portal.is_complete = True
            portal.save()
            return redirect('/roboexpo/registration/')

        return render(request,'complete-profile.html',{'message':"Please complete your details first"})

    r = Roboexpo.objects.all()
    for i in r:
        if i.selected==None and not i.mail_delivered:
            #print(i.id, i.team_name, [i.team_mates.all()], i.selected)
            continue
        elif i.selected==True and not i.mail_delivered:
            #print(i.id, i.team_name, [i.team_mates.all()], i.selected)
            mail_sender(True, i.id)
        elif i.selected==False and not i.mail_delivered:
            #print(i.id, i.team_name, [i.team_mates.all()], i.selected)
            mail_sender(False, i.id)


    context = {
        'r': Roboexpo.objects.all(),
    }
    return render(request, 'roboexpo-registration.html', context)

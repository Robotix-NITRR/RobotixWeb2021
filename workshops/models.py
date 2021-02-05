from django.db import models

# Create your models here.
# class recruitment(models.Model):
#     name = models.CharField(max_length=110)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     whatsapp = models.CharField(max_length=15)
#     college = models.CharField(max_length=100)
#     branch = models.CharField(max_length=50)
#     sem = models.CharField(max_length=50)
#
#     tshirtcombo = models.CharField(max_length=10)
#     mode_payment = models.CharField(max_length=10)
#     transaction = models.CharField(max_length=30)
    # technical = models.BooleanField(default='False')
    # management = models.BooleanField(default='False')
    # design = models.BooleanField(default='False')
    # webD = models.BooleanField(default='False')
    # appD = models.BooleanField(default='False')
    # doc = models.BooleanField(default='False')
    # spons = models.BooleanField(default='False')
    # questions
    # intro = models.CharField(max_length=1000,default='')
    # responsibility =  models.CharField(max_length=1000,default='')
    # strength = models.CharField(max_length=1000,default='')
    # techskill = models.CharField(max_length=1000,default='')
    # join = models.CharField(max_length=1000,default='')
    # improve = models.CharField(max_length=1000,default='')
    # residence = models.CharField(max_length=50,default='')
    # transport = models.CharField(max_length=50,default='')
    # def __str__(self):
    #     return self.name


class ca(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    sem = models.CharField(max_length=50)
    reason = models.TextField(max_length=500,default='')
    rating = models.TextField(max_length=500,default='')
    # tshirtcombo = models.CharField(max_length=10)
    # mode_payment = models.CharField(max_length=10)
    # transaction = models.CharField(max_length=30)
    # technical = models.BooleanField(default='False')
    # management = models.BooleanField(default='False')
    # design = models.BooleanField(default='False')
    # webD = models.BooleanField(default='False')
    # appD = models.BooleanField(default='False')
    # doc = models.BooleanField(default='False')
    # spons = models.BooleanField(default='False')
    # questions
    # intro = models.CharField(max_length=1000,default='')
    # responsibility =  models.CharField(max_length=1000,default='')
    # strength = models.CharField(max_length=1000,default='')
    # techskill = models.CharField(max_length=1000,default='')
    # join = models.CharField(max_length=1000,default='')
    # improve = models.CharField(max_length=1000,default='')
    # residence = models.CharField(max_length=50,default='')
    # transport = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.name

class recruitment(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    branch = models.CharField(max_length=30)
    semester = models.CharField(max_length=100)
    domain = models.CharField(max_length=200)
    # pr = models.BooleanField(default=False)
    # spons = models.BooleanField(default=False)
    # tech = models.BooleanField(default=False)
    # web_app = models.BooleanField(default=False)
    # design_video = models.BooleanField(default=False)
    intro = models.TextField(max_length=1000)
    other_club_committee = models.TextField(max_length=1000)
    strength_weakness = models.TextField(max_length=1000)
    work = models.TextField(max_length=1000)
    why_robotix = models.TextField(max_length=1000)
    improvements_suggesions = models.TextField(max_length=1000)
    residence = models.CharField(max_length=100)
    priority = models.CharField(max_length=5)
    priority_reason = models.TextField(max_length=1000)
    task_completion = models.CharField(max_length=5)
    task_completion_reason = models.TextField(max_length=1000)
    intention = models.CharField(max_length=5)
    intention_reason = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Timer(models.Model):
    start = models.DateTimeField()
    stop = models.DateTimeField()

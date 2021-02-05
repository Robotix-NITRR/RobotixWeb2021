from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings

User = settings.AUTH_USER_MODEL


class portalUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name="portal",on_delete= models.CASCADE)
    # verified = models.BooleanField(default= False)
    is_complete = models.BooleanField(default= False)
    college = models.CharField(max_length= 150, null= True, blank= True)
    branch = models.CharField(max_length= 150, null= True, blank= True)
    semester = models.CharField(max_length=20,null= True, blank= True)
    # description = models.TextField(blank= True,null= True)
    joined_team = models.BooleanField(default= False)
    user_team_id = models.IntegerField(blank= True, null= True)
    is_admin = models.BooleanField(default= False)#team admin
    is_member = models.BooleanField(default= False)#robotics team member
    def __str__(self):
        return self.user.email + " extended portalUser class"

    USERNAME_FIELD = 'email'

# class UserLink(models.Model):
#     link = models.ForeignKey(User, on_delete= models.CASCADE)


# class Token(models.Model):
#     token = models.CharField(max_length=150)
class problem_statement(models.Model):
    title = models.CharField(max_length= 150, null= True, blank= True)
    domain = models.CharField(default='',max_length=100)
    description = models.TextField(max_length=10000,default='')
    requirements = models.TextField(max_length=10000)
    # xfile = models.FileField(null= True, blank= True,upload_to='robothonAbstract/')

class Team(models.Model):
    name = models.CharField(blank = True, null= True, max_length= 150)
    admin = models.OneToOneField(User, related_name= "leader", on_delete = models.CASCADE)
    member = models.ManyToManyField(User, related_name= "member")
    token = models.CharField(max_length= 100,null= True, blank= True)
    selected = models.BooleanField(default= False)
    abstract = models.FileField(upload_to='docs/robothon/abstracts',null=True)
    confirmed = models.BooleanField(default= False)

    def __str__(self):
        return "Team" + self.name
# Create your models here.

from django.db import models

# Create your models here.
class FYI(models.Model):
    head = models.CharField(max_length=50,default='')
    title = models.CharField(max_length=100)
    link = models.URLField()
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.head


class DIY(models.Model):

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='img/diy')
    desc = models.CharField(max_length=1000)
    mentor = models.CharField(max_length=50)
    members = models.CharField(max_length=200)
    file = models.FileField(upload_to='docs/diy',default='')

    def __str__(self):

        return self.title


class sponsors(models.Model):
    name = models.CharField(max_length= 150, null= True, blank= True)
    sponsor_type = models.CharField(max_length= 150, null= True, blank= True)
    website = models.CharField(max_length= 150, null= True, blank= True)
    phone_number = models.IntegerField(null= True, blank= True)
    logo = models.FileField(null= True, blank= True,upload_to='sponsors/')

    def __str__(self):
        return self.name

class web(models.Model):
    img = models.ImageField(upload_to='webteam',default='')
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    linkedin = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name

class app(models.Model):
    img = models.ImageField(upload_to='webteam',default='')
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    linkedin = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name


# class robothonAbstract(models.Model):
#     title = models.CharField(max_length= 150, null= True, blank= True)
#     xfile = models.FileField(null= True, blank= True,upload_to='robothonAbstract/')


# class roboExpoAbstract(models.Model):
#     title = models.CharField(max_length= 150, null= True, blank= True)
#     xfile = models.FileField(null= True, blank= True,upload_to='robothonExpoAbstract/')

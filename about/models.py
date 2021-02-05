from django.db import models

# Create your models here.
class Convenor(models.Model):
    photo = models.ImageField(upload_to='img/convenors')
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    fb_id = models.URLField()
    mail_id = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HeadCoordinator(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    fb_id = models.URLField()
    mail_id = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    fb_id = models.URLField()
    mail_id = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Coordinator(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    fb_id = models.URLField()
    mail_id = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Workshop(models.Model):
    photo = models.ImageField(upload_to='img/workshop')
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

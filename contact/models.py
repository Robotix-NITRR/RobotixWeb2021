from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=110)
    email = models.EmailField()
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

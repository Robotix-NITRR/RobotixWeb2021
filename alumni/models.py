from django.db import models

# Create your models here.
class Alumni(models.Model):

    year = models.IntegerField()
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name

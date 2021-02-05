from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Roboexpo(models.Model):
    team_name = models.CharField(max_length=150)
    email = models.EmailField()
    team_mates = models.ManyToManyField(User, related_name= "team_mates", null=True)
    selected = models.NullBooleanField(null=True)
    bid = models.IntegerField(default=0)
    mail_delivered = models.BooleanField(default=False)
    abstract = models.FileField(upload_to='docs/roboexpo/abstracts')
    def __str__(self):
        return self.team_name

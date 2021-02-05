from django.db import models
from django.db.models import fields
from .models import Certificate
from django import forms

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('url_key',)



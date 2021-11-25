from django.db import models

class PersonalData(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=False)
    phone = models.CharField(max_length=20, blank=True, null=False )

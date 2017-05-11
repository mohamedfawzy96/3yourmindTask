from django.db import models

class Companies(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    location = models.CharField(max_length=100,null=False,blank=False)

# Create your models here.

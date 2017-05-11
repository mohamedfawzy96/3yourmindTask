from django.db import models
from companies.models import Companies
'''

'''
class Materials(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    color = models.CharField(max_length=100,null=False,blank=False)
    transparent = models.BooleanField(default=False)
    supplier = models.ForeignKey(Companies , on_delete=models.CASCADE)
    price = models.FloatField()

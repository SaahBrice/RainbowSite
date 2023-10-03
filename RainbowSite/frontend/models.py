from django.db import models
from accounts.models import Secretary
# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

class blog(models.Model):
    author = models.ForeignKey(Secretary,blank=True, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(blank=True, max_length=50, default='My awesome post')
    image = models.ImageField(upload_to='blog',blank=True, null=True)
    description = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.title

class result(models.Model):
    f1 = models.ImageField(upload_to='results',blank=True, null=True)
    f2 = models.ImageField(upload_to='results',blank=True, null=True)
    f3 = models.ImageField(upload_to='results',blank=True, null=True)
    f4 = models.ImageField(upload_to='results',blank=True, null=True)
    f5 = models.ImageField(upload_to='results',blank=True, null=True)
    lss = models.ImageField(upload_to='results',blank=True, null=True)
    lsa = models.ImageField(upload_to='results',blank=True, null=True)
    usa = models.ImageField(upload_to='results',blank=True, null=True)
    usl = models.ImageField(upload_to='results',blank=True, null=True)
    active=models.BooleanField(default=False)
    def __str__(self):
        return self.title
    

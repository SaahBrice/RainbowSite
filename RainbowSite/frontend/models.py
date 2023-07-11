from django.db import models
from accounts.models import Secretary
# Create your models here.


class blog(models.Model):
    author = models.ForeignKey(Secretary,blank=True, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(blank=True, max_length=50, default='My awesome post')
    image = models.ImageField(upload_to='blog',blank=True, null=True)
    description = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.title
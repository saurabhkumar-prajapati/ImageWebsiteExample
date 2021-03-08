from django.db import models
from datetime import datetime

# Create your models here.
class Newuser(models.Model):
    event_name=models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='images/',blank=True)
    location=models.CharField(max_length=200,blank=True)
    date=models.DateTimeField(default=datetime.now(),blank=True)

    def  __str__(self):
        return self.event_name


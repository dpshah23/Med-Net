from django.db import models
import datetime
import django.utils.timezone

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=15)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
class appointments(models.Model):
    doc_email = models.CharField(max_length=200)
    p_email = models.CharField(max_length=200 , default=None)
    date = models.DateField()
    time = models.TimeField()
    specialization = models.CharField(max_length=100)
    payment = models.CharField(max_length=10)
    vc_link = models.TextField(default=None)
    completed = models.BooleanField(default=False)
    doc_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return "{doc_email} and {p_email}"
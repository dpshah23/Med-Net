from django.db import models
import datetime
import django
import django.utils
import django.utils.timezone

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=15)
    message=models.TextField()
    date=models.DateField(default=django.utils.timezone.now())

    def __str__(self):
        return self.name
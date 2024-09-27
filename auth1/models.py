from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone   


# Create your models here.
class User(models.Model):
    id=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    role=models.CharField(choices=["patient","doctor"],max_length=100)
    created_at=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    

class Visit(models.Model):
    page_visited = models.CharField(max_length=255, unique=True)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.page_visited} - {self.visit_count}"
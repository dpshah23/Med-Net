import django
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone   


# Create your models here.
class User(models.Model):
    id=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    state = models.CharField(max_length=50)
    dp = models.TextField()
    timestamp=models.DateTimeField()


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
    
class doctor(models.Model):
    email=models.EmailField()
    license_expiry = models.DateField()
    specialization = models.CharField(max_length=200)
    experience = models.DateField()
    qualification = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
class patient(models.Model):
    email=models.EmailField()
    emergency_n = models.CharField(max_length=100)
    emergency_no = models.CharField(max_length=15)
    blood_grp = models.CharField(max_length=5)
    medical_history = models.TextField()
    allergies = models.TextField()
    current_med = models.BooleanField(default=False)
    addiction = models.TextField()
    occupation = models.CharField(max_length=200)
    
    def __str__(self):
        return self.email 
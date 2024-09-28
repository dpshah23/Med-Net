from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import random
import string
import datetime

# Create your views here.

def login(request):

    if 'email'in request.session:
        return redirect('/')

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=User.objects.get(email=email)
            if user.check_password(password):
                request.session['email']=user.email
                request.session['name']=user.name
                request.session['id']=user.id
                messages.success(request,"Login Successful")
                return redirect('/')

              
            else:
                return render(request,'LoginDoctor.html',{'error':'Invalid Password'})
            
        
        except User.DoesNotExist:
            return render(request,"LoginDoctor.html",{"error":"User Does not Exist"})
        
    return render(request,'LoginDoctor.html')

def signup_doc(request):
    if 'email'in request.session:
        return redirect('/')
    
    if request.method=="POST":
        
        role=request.GET.get("role")
        fname=request.POST.get("fname")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        
        state=request.POST.get("state")
        
        expiry=request.POST.get("license_expiry")
        
        specialization=request.POST.get("specialization")
        startdate=request.POST.get("startdate")
        qualification=request.POST.get("highestqual")
        hospital=request.POST.get("hospital")
        license_no=request.POST.get("licenseno")
        
        password=request.POST.get("password")
        id=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(16))
        
        # birthdt=
        users=User(id=id,email=email,password=password,name=fname,role=role,dob=dob,phone=phone,state=state,dp=None,timestamp=datetime.datetime.now().today())
        users.save()
        
        doctors = doctor(expiry = expiry , specialization = specialization , startdate = startdate , qualification = qualification , hospital=hospital , license_no = license_no)
        doctors.save()
        
        return redirect('LoginDoctor.html')
    
    
def signup_p(request):
    if 'email'in request.session:
        return redirect('/')
    
    if request.method=="POST":
        
        role=request.GET.get("role")
        fname=request.POST.get("fname")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        state=request.POST.get("state")
        emergency_n = request.POST.get("emergency_n")
        emergency_no = request.POST.get("emergency_no")
        blood_grp = request.POST.get("blood_grp")
        medical_history = request.POST.get("medical_history")
        allergies = request.POST.get("allergies")
        addiction = request.POST.get("addiction")
        current_med = request.POST.get("current_med")
        occupation = request.POST.get("occupation")
        
        password=request.POST.get("password")
        id=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(16))
        timestamp=datetime.datetime.now().today()
        
        users=User(id=id,email=email,password=password,name=fname,role=role,dob=dob,phone=phone,state=state,dp=None,timestamp=timestamp)
        users.save()
        patients =patient(email = email , emergency_n = emergency_n , emergency_no=emergency_no , blood_grp = blood_grp , medical_history = medical_history , allergies = allergies , occupation = occupation)
        patients.save()
        
        return redirect ('LoginPatient.html')
 


def logout(request):
    if 'email' not in request.session:
        return redirect('/auth/login/')
    del request.session['email']
    del request.session['name']
    del request.session['id']
    messages.success(request,"Logout Successful")
    return redirect('/auth/login/')


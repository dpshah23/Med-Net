from django.shortcuts import render
from auth1.models import *
from home.models import appointments
import os
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dotenv import load_dotenv
import razorpay
from auth1.models import *
from home.models import appointments

# Create your views here.

# Create your views here.
def searchdoctor(request):

    if request.method=="POST":
        specialize=request.POST.get('specialize')

        doctors=doctor.objects.filter(specialization=specialize)

        return render(request,"DashboardDoctor.html",{'doctors':doctors})
    
    else:

        doctors=doctor.objects.all()
        return render(request,"DashboardDoctor.html")
    
def getallappointments(request):

    patient_email=request.SESSION.get('email')  
    appointments=appointments.objects.filter(p_email=patient_email)

    return render(request,"patientappoinment.html",{'appointments':appointments})

def bookappointment(request):
    
        if request.method=="POST":
            doctor_id=request.POST.get('doctor_id')
            date=request.POST.get('date')
            time=request.POST.get('time')
            patient_email=request.SESSION.get('email')
    
            appointment=appointments.objects.get(doctor_id=doctor_id,date=date,time=time)

            appointment.p_email=patient_email
            appointment.payment="Done"
            appointment.vc_link=None
            appointment.completed=False
            appointment.doc_paid=False
            appointment.save()
    
            return render(request,"patientappoinment.html")
    
        return render(request,"bookappointment.html")

def dashboard(request):
     
    cardiology=doctor.objects.filter(specialization="Cardiology")
    dermatology=doctor.objects.filter(specialization="Dermatology")
    pediatrics=doctor.objects.filter(specialization="Pediatrics")
    neurology=doctor.objects.filter(specialization="Neurology")
    orthopedics=doctor.objects.filter(specialization="Orthopedics")
    oncology=doctor.objects.filter(specialization="Oncology")
    psychiatry=doctor.objects.filter(specialization="Psychiatry")

    data = [
    {"name": "Cardiology", "doctors": cardiology.count() if cardiology.exists() else 0},
    {"name": "Dermatology", "doctors": dermatology.count() if dermatology.exists() else 0},
    {"name": "Pediatrics", "doctors": pediatrics.count() if pediatrics.exists() else 0},
    {"name": "Neurology", "doctors": neurology.count() if neurology.exists() else 0},
    {"name": "Orthopedics", "doctors": orthopedics.count() if orthopedics.exists() else 0},
    {"name": "Oncology", "doctors": oncology.count() if oncology.exists() else 0},
    {"name": "Psychiatry", "doctors": psychiatry.count() if psychiatry.exists() else 0}
]


    
    return render(request,"patientdashboard.html",{"length_doctors":data})  


    
def pay (request , id):
    
    ispaid = appointments.objects.get(id = id).paid_status
    load_dotenv()
    key = os.getenv('api_key_razorpay')
    secret = os.getenv('api_secret_razorpay')
    client = razorpay.Client(auth=(key, secret))
    pay = appointments.objects.get(id =id).payment
    
    if ispaid:
        return HttpResponse("Payment is already done")
    
    else:
        try:
            payment= client.order.create({"amount":pay , "currency": "INR", "payment_capture": '1'})
        except Exception as e:
            print("Error creating order: ", e)
            
    return render(request , "payment.html" , {'payment' : payment , 'key' : key})
    
    return redirect('bookappointment')
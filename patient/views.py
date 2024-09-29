import os
from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from dotenv import load_dotenv
import razorpay
from auth1.models import *
from home.models import appointments

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
from django.shortcuts import render
from auth1.models import *
from home.models import appointments
# Create your views here.

def getallotappointment(request):

    if request.method=="POST":
        doctor_id=request.SESSION.get('doctor_id')
        date=request.POST.get('date')
        time=request.POST.get("time")

        for i in time:
            appointment=appointments(doctor_id=doctor_id,date=date,time=i,p_email=None,time=None,specialization=None,payment=None,vc_link=None,completed=False,doc_paid=False)
            appointment.save()
        print(doctor_id,date,time)
    return render(request,"allotappointment.html")

# def getallappointments(request):
#     doc_id=request.SESSION.get('doctor_id')

#     appointments=appointments.objects.filter(doc_email=doc_id,completed=False,not_expired=True)
#     return render(request,"dashboardDoctor.html",{'appointments':appointments})
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
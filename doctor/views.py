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

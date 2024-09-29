from django.shortcuts import render,redirect
from .models import ContactUs
from django.http import JsonResponse
from dotenv import load_dotenv
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import json
import os
from .models import *
from auth1.models import *

# Create your views here.
def home(request):

    length_doctors=doctor.objects.filter().count()
    length_patients=patient.objects.filter().count()
    length_appointments=appointments.objects.filter().count()

    print(length_doctors,length_patients,length_appointments)

    return render(request,"home.html",{'length_doctors':length_doctors,'length_patients':length_patients,'length_appointments':length_appointments})

def about(request):
    return render(request,"about.html")

def dashboard(request):
    if 'role' and 'email' not in request.session:
        return redirect('/auth/login/')
    
    return redirect('/dashboard/')

def contact(request):

    if request.method=="POST":
        fname=request.POST.get('name')
        lname=request.POST.get('lname')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        message=request.POST.get('message')
        print(fname,lname,mobile,email,message)

        contact=ContactUs(name=fname+" "+lname,email=email,mobile=mobile,message=message)

        
    return render(request,"contact.html")

@csrf_exempt
def api_response(request):
    if request.method=="POST":
        load_dotenv()
        api_key=os.getenv('API_KEY_GEMINI')
        data=json.loads(request.body)
        question = data.get('question', '')
        try:
            genai.configure(api_key=api_key)

            model = genai.GenerativeModel('gemini-pro')
            resp="You are a healthcare assistant. A patient describes their symptoms, and you need to provide a possible condition in 1 or 2 sentences. Only mention the possible condition without additional explanations.Dont give other answers rather than the possible condition and dont give answer to unusual questions just give answer that i am unable to answer and add reason to it.And Answer Of greeting and only include text dont include readme response"


            question=resp+question
            response = model.generate_content(question)
            print(response)
            return JsonResponse({'answer': response.text})

        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=500)
        
    else:
        print("Invalid method")
        return JsonResponse({'error':"Invalid method"})

def termsandconditions(request):
    return render(request,"Terms & Conditions.html")

def privacy_policy(request):
    return render(request,"Privacy_Policy.html")
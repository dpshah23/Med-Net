from django.shortcuts import render

# Create your views here.
def searchdoctor(request):

    if request.method=="POST":
        specialize=request.POST.get('specialize')
        
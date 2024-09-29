from django.urls import path
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("about/",about,name="about"),
    path("api_reply/",api_response,name="api_response"),
    path("terms-and-conditions/",termsandconditions,name="termsandconditions"),
    path('privacy-policy/',privacy_policy,name="privacypolicy"),
]

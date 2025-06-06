from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based views
def addAdmission(request):
    return HttpResponse('Here You Add Admission')

def admissionReport(request):
    return HttpResponse('Here You see Admissions')

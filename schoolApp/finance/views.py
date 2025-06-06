from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# function based views
def feeCollection(request):
    return HttpResponse('Here You collect fee')

def feeDue(request):
    return HttpResponse('Here You see fee due')

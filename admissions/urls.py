from django.urls import path
from admissions.views import addAdmission, admissionReport

urlpatterns = [

    path('newadm/',addAdmission),
    path('admrpt/',admissionReport),

]

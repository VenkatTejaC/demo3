from django.urls import path
from finance.views import feeCollection, feeDue

urlpatterns = [

    path('feecoll/',feeCollection),
    path('feedue/',feeDue),



]

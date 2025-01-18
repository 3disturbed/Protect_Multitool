from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account_home.models import EmergencyContact
import requests
import json
import os


# Create your views here.
def case_home(request):
    return render(request, 'cases/case_home.html')




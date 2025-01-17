from django.shortcuts import render, redirect
from django.urls import reverse

def home(request):
    
    return redirect('route_planner:planner')

def planner(request):
    
    return render(request, 'route_planner/planner.html')
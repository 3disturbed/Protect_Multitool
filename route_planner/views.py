from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import PlannedRouteForm
from .models import PlannedRoute
import requests
import json
import os

def home(request):
    
    return redirect('route_planner:planner')

@login_required
def planner(request):
    if request.method == 'POST':
        form = PlannedRouteForm(request.POST)
        if form.is_valid():
            planned_route = form.save(commit=False)
            planned_route.user = request.user
            planned_route.save()
        
            return redirect('route_planner:timer', id=planned_route.id)
    else:
        form = PlannedRouteForm()

    return render(request, 'route_planner/planner.html', {'form': form})


@login_required
def timer(request, id):
    try:
        planned_route = PlannedRoute.objects.get(id=id, user=request.user)
    except PlannedRoute.DoesNotExist:
        # Handle the case where the route doesn't exist
        return redirect('route_planner:planner')

    context = {
        'user': planned_route.user,
        'timer': planned_route.time_limit,
        'pin': planned_route.pin_code,
        'id': planned_route.id,
    }
    print(context['timer'])
    return render(request, 'route_planner/timer.html', context)
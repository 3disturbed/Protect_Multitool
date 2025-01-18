from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import PlannedRouteForm
from .models import PlannedRoute

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
            return redirect('route_planner:planner')
    else:
        form = PlannedRouteForm()

    return render(request, 'route_planner/planner.html', {'form': form})
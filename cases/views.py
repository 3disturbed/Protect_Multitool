from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account_home.models import EmergencyContact
from route_planner.models import PlannedRoute
import requests
import json
import os


# Create your views here.
def case_home(request):
    return render(request, 'cases/case_home.html')


@csrf_exempt
def emergency_lookup(request):
    if request.method == "POST":
        phone = request.POST.get('phone', '').replace(" ", "")
        secret_key = request.POST.get('secret_key', '').strip()

        # Debugging: Print inputs
        print(f"Phone: {phone}, Secret Key: {secret_key}")

        # Validate inputs
        if not phone or not secret_key:
            return render(request, 'cases/emergency_lookup.html', {'error': 'Both phone number and secret key are required.'})

        # Find the emergency contact
        contact = EmergencyContact.objects.filter(phone=phone).first()
        if not contact:
            return render(request, 'cases/emergency_lookup.html', {'error': 'No emergency contact found with this phone number.'})

        # Find the associated route
        route = PlannedRoute.objects.filter(secret_key=secret_key, user=contact.user).first()
        if not route:
            return render(request, 'cases/emergency_lookup.html', {'error': 'No route found for the provided secret key.'})

        # Pass route details to the template
        route_details = {
            'user': route.user.username,
            'firstname': route.user.first_name,
            'lastname': route.user.last_name,
            'starting_location': route.starting_location,
            'finishing_location': route.finishing_location,
            'with_who': route.with_who,
            'time_limit': route.time_limit,
            'additional_info': route.additional_info,
            'created_at': route.created_at.isoformat(),
        }
        print(f"Route details for user {route_details['user']}: {route_details}")
        return render(request, 'cases/emergency_lookup.html', {'route': route_details})

    # For GET requests or invalid methods, render the blank form
    return render(request, 'cases/emergency_lookup.html')

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import PlannedRouteForm
from .models import PlannedRoute
from account_home.models import EmergencyContact
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
    user = request.user
    if user.first_name:
        first_name = user.first_name
    else:
        first_name = 'me'

    emergency_contacts = EmergencyContact.objects.filter(user=user)
    emergency_contacts_list = []
    if emergency_contacts.exists():
        for contact in emergency_contacts:
            emergency_contacts_list.append({
                'name': contact.name,
                'phone_number': contact.phone,
            })
            print (emergency_contacts_list)
    else:
        print('No emergency contacts to display')

    emergency_contacts_json = json.dumps(emergency_contacts_list)

    try:
        planned_route = PlannedRoute.objects.get(id=id, user=request.user)
    except PlannedRoute.DoesNotExist:
        # Handle the case where the route doesn't exist
        return redirect('route_planner:planner')
    
    if planned_route.secret_key:
        secret_key = planned_route.secret_key
    
    context = {
        'emergency_contacts_list': emergency_contacts_json,
        'first_name': first_name,
        'user': planned_route.user,
        'timer': planned_route.time_limit,
        'pin': planned_route.pin_code,
        'id': planned_route.id,
    }
    return render(request, 'route_planner/timer.html', context)

@csrf_exempt
def verify_pin(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        id = data.get('id')
        planned_route = PlannedRoute.objects.get(id=id, user=request.user)
        user_pin = data.get('pin')
        actual_pin = planned_route.pin_code
        print(user_pin)
        print(actual_pin)  # Replace with dynamically fetched or securely stored pin
        if user_pin == actual_pin:
            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})


@csrf_exempt
def emergency_message(request):
    user = request.user
    accessKey = os.environ['ACCESS_KEY']
    namespaceId = os.environ['NAMESPACE_ID']
    channelId = os.environ['CHANNEL_ID']
    if request.method == 'POST':
        try:
 
            data = json.loads(request.body)
            recipient = data.get("recipient")
            sender = data.get("sender")
            contact = data.get("contact")
            id = data.get("id")
            planned_route = PlannedRoute.objects.get(id=id, user=request.user)
            if planned_route.secret_key:
                secret_key = planned_route.secret_key

            print(secret_key)

            actual_code = planned_route.pin_code


            if not recipient or not sender:
                return JsonResponse({"error": "Missing 'recipient' or 'sender' in the request body"}, status=400)


            external_url = "https://conversations.messagebird.com/v1/send"


            external_data = {
                "type": "hsm",
                "to": recipient,
                "from": channelId,
                "content": {
                    "hsm": {
                        "namespace": namespaceId,
                        "templateName": "test_sos_code",
                        "language": {
                            "policy": "deterministic",
                            "code": "en"
                        },
                        "params": [
                             {
                                "default": contact
                                                    },
                            {
                                "default": sender
                            },
                            {
                                "default": secret_key
                            }
                          ]
                    }
                }
            }


            headers = {
                "Authorization": os.environ['ACCESS_KEY'],
                "Content-Type": "application/json",
            }


            response = requests.post(external_url, json=external_data, headers=headers)

            if response.status_code == 202:
                return JsonResponse({"message": "Request to external API succeeded", "response": response.json()}, status=200)
            else:
                return JsonResponse(
                    {"error": "External API request failed", "details": response.text},
                    status=response.status_code
                )

        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=400)

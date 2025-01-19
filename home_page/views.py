from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account_home.models import EmergencyContact
from django.utils.decorators import method_decorator
import requests
import json
import os

import json
from django.shortcuts import render

def home(request):
    user = request.user
    emergency_contacts_list = []

    # Check if the user is authenticated
    if user.is_authenticated:
        first_name = user.first_name
        emergency_contacts = EmergencyContact.objects.filter(user=user)

        # If emergency contacts exist, populate the list
        if emergency_contacts.exists():
            for contact in emergency_contacts:
                emergency_contacts_list.append({
                    'name': contact.name,
                    'phone_number': contact.phone,
                })
        else:
            print('No emergency contacts to display')

        # Serialize the list to JSON
        emergency_contacts_json = json.dumps(emergency_contacts_list)

        # Prepare context with JSON and first_name
        context = {
            'emergency_contacts_list': emergency_contacts_json,
            'first_name': first_name,
        }
    else:
        # Anonymous users
        context = {
            'emergency_contacts_list': json.dumps([]),
            'first_name': None,
        }

    # Render the homepage
    return render(request, 'home_page/home.html', context)


def about(request):
    return render(request, 'home_page/about.html') 

@login_required
def profile_handler(request):
    # Check if the profile exists
    profile = Profile.objects.filter(user=request.user).first()

    if profile:
        # If the profile exists, render the profile detail page
        return render(request, 'home_page/profile_detail.html', {'profile': profile})
    else:
        # If no profile exists, redirect to the profile creation page
        return redirect('home_page:profile_create')


@login_required
def profile_create(request):
    # Check if the profile already exists
    if Profile.objects.filter(user=request.user).exists():
        # Redirect to profile detail if the profile already exists
        return redirect('home_page:profile_handler')

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            # Redirect to profile detail after creation
            return redirect('home_page:profile_handler')
    else:
        form = ProfileForm()

    # Render the profile creation form
    return render(request, 'home_page/profile_form.html', {'form': form})



@login_required
@csrf_exempt
def emergency_message(request):
    accessKey = os.environ['ACCESS_KEY']
    namespaceId = os.environ['NAMESPACE_ID']
    channelId = os.environ['CHANNEL_ID']
    if request.method == 'POST':
        try:

 
            data = json.loads(request.body)
            recipient = data.get("recipient")
            sender = data.get("sender")
            contact = data.get("contact")

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
                        "templateName": "test_sos_alert",
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




@login_required
@csrf_exempt
def emergency_message_coordinates(request):
    accessKey = os.environ['ACCESS_KEY']
    namespaceId = os.environ['NAMESPACE_ID']
    channelId = os.environ['CHANNEL_ID']
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON payload

            recipient = data.get("recipient")
            sender = data.get("sender")
            contact = data.get("contact")
            longitude = data.get("longitude_info")
            latitude = data.get("latitude_info")
            joinedUrl = f"{latitude},{longitude}"
            print(recipient, sender, contact, latitude, longitude, joinedUrl)

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
                        "templateName": "test_sos_coordinates_2",
                        "language": {
                            "policy": "deterministic",
                            "code": "en"
                        },
                          "components": [
                            {
                                "type": "body",
                                "parameters": [
                                    {
                                        "type": "text",
                                        "text": contact
                                    },
                                    {
                                        "type": "text",
                                        "text": sender
                                    },
                                    {
                                        "type": "text",
                                        "text": str(latitude)
                                    },
                                    {
                                        "type": "text",
                                        "text": str(longitude)
                                    },
                                ]
                            },
                                 {
                                    "type": "button",
                                    "sub_type": "url",
                                     "parameters": [
                                 {
                                    "type": "text",
                                    "text": joinedUrl
                                    }
                                 ]
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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account_home.models import EmergencyContact
import requests
import json
import os

# Create your views here.

@login_required
def simple_game_view(request):
    user = request.user
    first_name = user.first_name
    emergency_contacts = EmergencyContact.objects.filter(user=user)
    emergency_contacts_list = []
    print(user)
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
    print(emergency_contacts_json)
    context = {
        'emergency_contacts_list': emergency_contacts_json,
        'first_name': first_name,
    }


    return render(request, 'game/game.html', context)

@login_required
@csrf_exempt
def handle_event(request):
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
                        "templateName": "test_sos",
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
def handle_event_coordinates(request):
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
                        "templateName": "test_sos_coordinates",
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

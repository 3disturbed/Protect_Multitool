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
    print(user)
    emergency_contacts = EmergencyContact.objects.filter(user=user)

    if emergency_contacts.exists():
        emergency_contact = emergency_contacts.first()
        phone_number = emergency_contact.phone
        contact_name = emergency_contact.name
        print(phone_number, first_name)
    else:
        phone_number = None
        user_name = None
        print('Nothing to print')


    context = {
        'emergency_contacts': emergency_contacts,  
        'phone_number': phone_number,
        'contact_name': contact_name,
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
                        "templateName": "test_sos_2",
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

            if response.status_code == 200:
                return JsonResponse({"message": "Request to external API succeeded", "response": response.json()}, status=200)
            else:
                return JsonResponse(
                    {"error": "External API request failed", "details": response.text},
                    status=response.status_code
                )

        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred", "details": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method. Only POST is allowed."}, status=400)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account_home.models import EmergencyContact
import requests
import json
import os

# Create your views here.
def panic_main(request):
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

    return render(request, 'panic/panic.html', context)


@login_required
@csrf_exempt
def handle_panic_event(request):
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

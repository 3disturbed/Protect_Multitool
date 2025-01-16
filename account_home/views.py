from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmergencyContactForm
from .models import EmergencyContact

@login_required
def emergency_contact_list(request):
    contacts = EmergencyContact.objects.filter(user=request.user)
    return render(request, 'emergency_contacts/contact_list.html', {'contacts': contacts})

@login_required
def add_emergency_contact(request):
    if EmergencyContact.objects.filter(user=request.user).count() >= 5:
        return render(request, 'emergency_contacts/contact_limit.html')

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('emergency_contact_list')
    else:
        form = EmergencyContactForm()
    return render(request, 'emergency_contacts/add_contact.html', {'form': form})


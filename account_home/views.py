from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmergencyContactForm
from .models import EmergencyContact

@login_required
def emergency_contact_list(request):
    contacts = EmergencyContact.objects.filter(user=request.user)
    return render(request, 'account_home/contact_list.html', {'contacts': contacts})

@login_required
def add_emergency_contact(request):
    if EmergencyContact.objects.filter(user=request.user).count() >= 5:
        return render(request, 'account_home/contact_limit.html')

    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('emergency_contact_list')
    else:
        form = EmergencyContactForm()
    return render(request, 'account_home/add_contact.html', {'form': form})

@login_required
def edit_emergency_contact(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('emergency_contact_list')
    else:
        form = EmergencyContactForm(instance=contact)
    return render(request, 'account_home/edit_contact.html', {'form': form, 'contact': contact})

@login_required
def delete_emergency_contact(request, pk):
    contact = get_object_or_404(EmergencyContact, pk=pk, user=request.user)
    if request.method == 'POST':
        contact.delete()
        return redirect('emergency_contact_list')
    return render(request, 'account_home/delete_contact.html', {'contact': contact})
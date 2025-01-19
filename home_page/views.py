from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.utils.decorators import method_decorator

def home(request):
    return render(request, 'home_page/home.html')

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







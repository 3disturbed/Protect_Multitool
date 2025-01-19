from django.urls import path
from . import views

app_name = 'home_page'

urlpatterns = [
    path('', views.home, name='home'),  # Maps to the home view
    path('about/', views.about, name='about'),  # Maps to the about view
    path('profile/', views.profile_handler, name='profile_handler'),  # Handles profile logic (detail or redirect to create)
    path('profile/create/', views.profile_create, name='profile_create'),  # Handles profile creation
    path('emergency/', views.emergency_message, name='emergency_message'),
    path('emergency-coordinates/', views.emergency_message_coordinates, name="emergency_message_coordinates")
]

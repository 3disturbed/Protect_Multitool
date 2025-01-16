from django.urls import path
from . import views

urlpatterns = [
    path('', views.emergency_contact_list, name='emergency_contact_list'),
    path('add/', views.add_emergency_contact, name='add_emergency_contact'),
]

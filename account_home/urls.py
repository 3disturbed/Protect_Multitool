from django.urls import path
from . import views

urlpatterns = [
    path('emergencycontact/', views.emergency_contact_list, name='emergency_contact_list'),
    path('add-emergencycontact/', views.add_emergency_contact, name='add_emergency_contact'),
    path('edit-emergencycontact/<int:pk>/', views.edit_emergency_contact, name='edit_emergency_contact'),
    path('delete-emergencycontact/<int:pk>/', views.delete_emergency_contact, name='delete_emergency_contact'),
]

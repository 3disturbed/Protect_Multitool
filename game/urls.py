from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.simple_game_view, name='home'),
    path('handle-event/', views.handle_event, name='handle_event'),
    path('handle-event-location/', views.handle_event_coordinates, name='handle_event_coordinates')
]
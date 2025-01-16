from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_game_view, name='game'),
    path('handle-event/', views.handle_event, name='handle_event'),
]
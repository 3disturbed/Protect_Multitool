from django.urls import path
from . import views

app_name = 'panic'

urlpatterns = [
    path('', views.panic_main, name='panic_main'),
    path('panic-button/', views.handle_panic_event, name="handle_panic_event")
]
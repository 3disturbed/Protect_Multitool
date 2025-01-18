from django.urls import path
from . import views

app_name = 'cases'

urlpatterns = [
    path('', views.case_home, name='case_viewer_main'),
]
from django.urls import path
from . import views

app_name = 'route_planner'

urlpatterns = [
   path('', views.home, name='home'),  # This will redirect to your main route planner page,
   path('planner/', views.planner, name='planner'),  # Your actual route planner page
   path('timer/<int:id>/', views.timer, name='timer'),
   path('timer/verify-pin/', views.verify_pin, name='verify_pin'),
   path('timer/emergency-message/', views.emergency_message, name='emergency_message'),
]
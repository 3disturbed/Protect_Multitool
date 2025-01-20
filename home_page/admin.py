from django.contrib import admin
from home_page.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone_number')  # Include last_name
    fields = ('user', 'first_name', 'last_name', 'phone_number')  # Include last_name



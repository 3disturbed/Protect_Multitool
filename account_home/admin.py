from django.contrib import admin
from .models import EmergencyContact
# Register your models here.

class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'phone', 'relationship') 
    search_fields = ('name', 'phone', 'relationship')  

admin.site.register(EmergencyContact, EmergencyContactAdmin)
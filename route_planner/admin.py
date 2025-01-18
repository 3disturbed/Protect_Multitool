from django.contrib import admin

# Register your models here.
from .models import PlannedRoute

@admin.register(PlannedRoute)
class PlannedRouteAdmin(admin.ModelAdmin):
    list_display = ('user', 'starting_location', 'finishing_location', 'time_limit', 'created_at')
    search_fields = ('user__username', 'starting_location', 'finishing_location', 'with_who')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('secret_key',)
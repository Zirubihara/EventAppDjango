from django.contrib import admin
from .models import Event
# Register your models here.

class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Event, EventsAdmin)
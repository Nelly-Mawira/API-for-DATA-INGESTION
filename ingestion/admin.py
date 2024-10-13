from django.contrib import admin
from .models import DataEntry

# Register your models here.

admin.site.register(DataEntry)

class DataEntryAdpupmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id',)

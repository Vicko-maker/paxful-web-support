from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('id', 'email', 'username')  # Replace with actual fields from your model
    list_filter = ('email',)  # Optional: Adds filters for specific fields
    search_fields = ('email', 'username')  # Optional: Adds a search box

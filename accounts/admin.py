from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """ Admin class that contains the Profile model
        configurations.
    """


# Register to admin panel
admin.site.register(Profile, ProfileAdmin)
from django.contrib import admin
from .models import ProfileData

@admin.register(ProfileData)
class ProfileDataAdmin(admin.ModelAdmin):
    list_display=('profile','prediction',)

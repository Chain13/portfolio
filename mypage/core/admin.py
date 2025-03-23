from django.contrib import admin
from .models import UserProfile
# Register your models here.
# Django Admin Configuration
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user' , 'birthday')
    search_fields = ('user__username',)


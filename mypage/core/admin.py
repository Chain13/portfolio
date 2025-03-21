from django.contrib import admin
from .models import Blog, BlogContent, Tag,UserProfile
# Register your models here.
# Django Admin Configuration
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user' , 'birthday')
    search_fields = ('user__username',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(BlogContent)
class BlogContentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'content_type', 'order')
    list_filter = ('content_type',)
    search_fields = ('blog__title', 'text', 'code')

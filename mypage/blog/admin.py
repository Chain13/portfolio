from django.contrib import admin
from .models import Blog, Tag
from .forms import BlogForm
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    form = BlogForm
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set created_by during creation, not on updates
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
        
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
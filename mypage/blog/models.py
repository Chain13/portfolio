from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', editable=False)
    tags = models.ManyToManyField('Tag', blank=True, related_name='blogs')
    cover = models.ImageField(upload_to='blog_covers/', blank=True, null=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

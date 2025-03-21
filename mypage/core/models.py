from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        UserProfile.objects.get_or_create(user=instance)  # Ensure profile exists

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):  # Avoid errors if profile doesn't exist
        instance.profile.save()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField('Tag', blank=True, related_name='blogs')
    cover = models.ImageField(upload_to='blog_covers/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class ContentType(models.TextChoices):
    TEXT = 'text', 'Text'
    IMAGE = 'image', 'Image'
    VIDEO = 'video', 'Video'
    CODE = 'code', 'Code'
    SEPARATOR = 'separator', 'Separator'
class CodeLanguage(models.TextChoices):
    PYTHON = 'python', 'Python'
    JAVA = 'java', 'Java'
    JAVASCRIPT = 'javascript', 'JavaScript'
    BASH = 'bash', 'Bash'
    C = 'c', 'C'
    CPP = 'cpp', 'C++'
    RUBY = 'ruby', 'Ruby'
    GO = 'go', 'Go'
    PHP = 'php', 'PHP'
class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='contents')
    content_type = models.CharField(max_length=20, choices=ContentType.choices)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)  # Store video URLs (e.g., YouTube links)
    code = models.TextField(blank=True, null=True)
    code_language = models.CharField(max_length=20, choices=CodeLanguage.choices, blank=True, null=True)

    order = models.PositiveIntegerField(default=0, editable=False)
    
    class Meta:
        ordering = ['order']
    def save(self, *args, **kwargs):
        if not self.pk:
            last_order = BlogContent.objects.filter(blog=self.blog).aggregate(models.Max('order'))['order__max']
            self.order = (last_order + 1) if last_order is not None else 0
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.blog.title} - {self.content_type} ({self.order})'
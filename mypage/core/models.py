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


"""
@authors Alexander Fisher
@version Barbell Version 1.2

@about Models definition for the Barbell application, structuring the database schema and relationships. 
       This module contains classes representing different aspects of the application's data model,
       including user profiles, groups, stat data, and images, with their respective fields and behaviors.

        *CustomUser:
            - Extends Django's AbstractUser to include additional fields like profile pictures, biographies, date of birth, phone numbers, and gender.
            - Incorporates a choice field for gender with options for Male, Female, and Other.
            - Associates users with groups and maintains a points system for gamification purposes.

        *Group:
            - Represents user-created groups with attributes for name, biography, and privacy settings.
            - Supports two privacy options: Public and Private, controlled via a choice field.
            - Groups are created by users, establishing a link between the group and its creator.

        *Meta Information:
            - Each model class includes meta information to define human-readable names for the Django admin interface.
            - Ensures clarity and ease of management for site administrators.

        *String Representation:
            - Implements the `__str__` method for each class to return a meaningful string representation,
              improving readability and convenience during debugging and administration.

        *Relationships:
            - Demonstrates the use of Django model relationships, including ForeignKey and ManyToManyField,
              to model complex data structures and interactions between different entities within the application.

        *Customization and Extensibility:
            - The models are designed to be flexible and extensible, allowing for future enhancements and additional features
              as the application evolves and grows in complexity.
"""

from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import AbstractUser, Permission, Group as MyGroup
from google.cloud import storage
import os

def user_directory_path(instance, filename):
    return 'userProfilePictures/user_{0}/{1}/{2}/{3}'.format(instance.username, now().year, now().month, filename)

class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    current_group = models.ForeignKey('Group', related_name='group_members', null=True, blank=True, on_delete=models.SET_NULL)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    profile_picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def delete_file_from_gcs(self, file_path):
        if not file_path:
            return
        
        try:
            storage_client = storage.Client(credentials=settings.GS_CREDENTIALS)
            bucket_name = os.getenv('GS_BUCKET_NAME', 'barbell_bucket_1')
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(file_path)

            if blob.exists():
                blob.delete()
                print(f"Deleted {file_path} from {bucket_name}")
            else:
                print(f"{file_path} does not exist in {bucket_name}")

        except Exception as e:
            print(f"Error deleting {file_path} from GCS: {e}")

    def save(self, *args, **kwargs):
        try:
            this = CustomUser.objects.get(id=self.id)
            if this.profile_picture != self.profile_picture:
                old_file_path = this.profile_picture.name
                self.delete_file_from_gcs(old_file_path)
        except CustomUser.DoesNotExist:
            pass  
        super(CustomUser, self).save(*args, **kwargs)
        
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    points = models.IntegerField(default=0) 
    class Meta:
        verbose_name = 'App user'
        verbose_name_plural = 'App users'
    def __str__(self):
        return self.username
    
class Group(models.Model):
    name = models.CharField(max_length=255)
    groupbio = models.TextField(default='')
    PRIVACY_CHOICES = [
        ('PUB', 'Public'),
        ('PRV', 'Private'),
    ]
    privacy = models.CharField(max_length=3, choices=PRIVACY_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Workout(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    day = models.CharField(max_length=3, choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('T', 'Thursday'), ('F', 'Friday'), ('S', 'Saturday'), ('S', 'Sunday')], blank=True, null=True)
    order = models.IntegerField(default=0)
    
class ImageMetadata(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else 'Image'
    
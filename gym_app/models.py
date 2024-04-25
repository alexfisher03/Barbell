"""
@authors Alexander Fisher & Jonathan Salem
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

        *TableData:
            - Stores user-specific data entries with attributes for date, title, and value.
            - Designed to accommodate various types of numerical data associated with user activities.

        *StatData:
            - Specifically tailored for tracking workout statistics, including the exercise name, number of sets, and repetitions.
            - Facilitates the recording and analysis of users' fitness progress over time.

        *ImageMetadata:
            - Manages image uploads by users, with fields for the associated user, image file, caption, and timestamp.
            - Enables the sharing and display of images within the application, enhancing user interaction and content richness.

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

        *Best Practices:
            - Follows Django model best practices, ensuring a robust, scalable, and maintainable database schema
              that effectively supports the application's functionality and user requirements.
"""

from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import AbstractUser, Permission, Group as MyGroup

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
    profile_picture = models.ImageField(
        upload_to=user_directory_path,
        null=True,
        blank=True
    )
    def save(self, *args, **kwargs):
        try:
            this = CustomUser.objects.get(id=self.id)
            if this.profile_picture != self.profile_picture:
                this.profile_picture.delete(save=False)
        except: pass  # when new photo is added, it will not be in the database yet
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

class TableData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    data_title = models.CharField(max_length=100)
    data_value = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = 'Stat Data'
        verbose_name_plural = 'Stat Data'

    def __str__(self):
        return self.data_title
    
class StatData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=20)
    num_sets = models.IntegerField()
    num_reps = models.IntegerField()
    
class ImageMetadata(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else 'Image'
    
    
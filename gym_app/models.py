"""
@author Alexander Fisher & Jonathan Salem
@version Barbell Version 1

@about This is the Python script handling our database data table *actual* data. 
       Each class object corresponds to an object containing our user's data, a user's group,
       user stat or stat table, etc. 
"""

from django.db import models
from django.conf import settings
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import AbstractUser, Permission, Group as MyGroup

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
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
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
    
    
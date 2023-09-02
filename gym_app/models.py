from django.db import models
from django.conf import settings
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import AbstractUser, Permission, Group


class CustomUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    class Meta:
        verbose_name = 'App user'
        verbose_name_plural = 'App users'

    # Other fields like date_of_birth, bio, etc.
    def __str__(self):
        return self.username
    
class Group(models.Model):
    groupname = models.CharField(max_length=255)
    groupbio = models.TextField()
    PRIVACY_CHOICES = [
        ('PUB', 'Public'),
        ('PRV', 'Private'),
    ]
    privacy = models.CharField(max_length=3, choices=PRIVACY_CHOICES)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.groupname

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
    
class ImageMetadata(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else 'Image'
    
    
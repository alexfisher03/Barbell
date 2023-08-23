from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Additional fields if needed
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    # Other fields like date_of_birth, bio, etc.

    def __str__(self):
        return self.username

class TableData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_title = models.CharField(max_length=100)
    data_value = models.DecimalField(max_digits=10, decimal_places=2)
    # Other fields as needed

    def __str__(self):
        return self.data_title
    
class ImageMetadata(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption if self.caption else 'Image'
    
    
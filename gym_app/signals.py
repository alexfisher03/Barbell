"""
@author Alexander Fisher & Jonathan Salem
@version Barbell Version 1

@about Handlers for signals sent by Django ORM system.
       This setup ensures that when a CustomUser instance is deleted, 
       any associated log entries in the admin log that reference this user 
       are also removed, maintaining the integrity and cleanliness of data and logs.
"""

from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from .models import CustomUser

@receiver(pre_delete, sender=CustomUser)
def delete_related_logs(sender, instance, **kwargs):
    print("delete_related_logs Signal Executed")
    LogEntry.objects.filter(user_id=instance.id).delete()



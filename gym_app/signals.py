from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry
from .models import CustomUser

@receiver(pre_delete, sender=CustomUser)
def delete_related_logs(sender, instance, **kwargs):
    print("delete_related_logs Signal Executed")
    LogEntry.objects.filter(user_id=instance.id).delete()



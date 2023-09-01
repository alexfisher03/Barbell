from django.apps import AppConfig
from django.db.models.signals import pre_delete


class GymAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym_app'

    def ready(self):
        print("**--%$ Welcome To Barbell $%--**")
        from gym_app.models import CustomUser
        from gym_app.signals import delete_related_logs
        pre_delete.connect(delete_related_logs, sender=CustomUser)



from django.apps import AppConfig
from django.db.models.signals import pre_delete


class GymAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym_app'

    def ready(self):
        print("        ~+")
        print("                *       +")
        print("          '                  |")
        print('      ()    .-.,="``"=.    - o -')
        print("            '=/_       \     |")
        print("         *   |  '=._    |")
        print("              \     `=./`,        '")
        print("           .   '=.__.=' `='      *")
        print("  +                         +")
        print("       O      *        '       .")
        print("__--**Successfully Initialized Barbell**--__")
        print("--________________________________________--")
        from gym_app.models import CustomUser
        from gym_app.signals import delete_related_logs
        pre_delete.connect(delete_related_logs, sender=CustomUser)



from django.apps import AppConfig
from django.db.models.signals import pre_delete


class GymAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym_app'

    def ready(self):
        print(' .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.')
        print('(     __        __   _                            _          ____    _    ____  ____  _____ _     _           )')
        print(' )    \ \      / ___| | ___ ___  _ __ ___   ___  | |_ ___   | __ )  / \  |  _ \| __ )| ____| |   | |         (  ')
        print("(      \ \ /\ / / _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  _ \ / _ \ | |_) |  _ \|  _| | |   | |          )")
        print( ')      \ V  V |  __| | (_| (_) | | | | | |  __/ | || (_) | | |_) / ___ \|  _ <| |_) | |___| |___| |___      (')
        print('(        \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |____/_/   \_|_| \_|____/|_____|_____|_____|      )')
        print(' )                                                                                                           (')
        print('(                                                                                                             )')
        print(' "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"')
        from gym_app.models import CustomUser
        from gym_app.signals import delete_related_logs
        pre_delete.connect(delete_related_logs, sender=CustomUser)



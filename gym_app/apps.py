from django.apps import AppConfig
from django.db.models.signals import pre_delete


class GymAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym_app'

    def ready(self):
        print("                         _                      _______                      _")
        print("                      _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_")
        print("                     dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb")
        print("                    V      ~\"Mb          dOOOOOOOOOOOOOOOOOb          dM\"~      V")
        print("                              `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'")
        print("                               `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'")
        print("                          __     `YMMM| OP'~\"YOOOOOOOOOOOP\"~`YO |MMMP'     __")
        print("                        ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.")
        print("                     _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb.")
        print("                                 `YMMMM\\`OOOo     OOO     oOOO'/MMMMP'")
        print("                         ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.")
        print("                       ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.")
        print("                      ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.")
        print("                      MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM")
        print("                      YMb           ~YMMMM\\`OOOOI`````IOOOOO'/MMMMP~           dMP")
        print("                       `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'")
        print("                         `'                  `OObNNNNNdOO'                   `'")
        print("                                               `~OOOOO~'                        ")
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



from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_screen, name='about'),
    path('creategroup/', views.creategroup_screen, name='create_group'),
    path('forgot_password/', views.forgotpassword_screen, name='forgot_password'),
    path('general_settings/', views.generalsettings_screen, name='general_settings'),
    path('group_screen/', views.group_screen, name='group_screen'),
    path('group_settings/', views.group_settings_screen, name='group_settings'),
    path('home/', views.home_screen, name='home'),
    path('init/', views.init_screen, name='init'),
    path('input_rep_stats/', views.input_rep_stats_screen, name='input_rep_stats'),
    path('privacy_screen/', views.privacy_screen, name='privacy'),
    path('profile/self/', views.profile_self_screen, name='profile_self'),
    path('profile/other/', views.profile_other_screen, name='profile_other'),
    path('profile/settings/', views.profilesettings_screen, name='profilesettings'),
    path('register/', views.register_screen, name='register'),
    path('signing/', views.signin_screen, name='singin'),
    path('table/', views.stat_screen, name='stat'),
]
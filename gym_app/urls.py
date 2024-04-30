"""
@author Alexander Fisher & Jonathan Salem
@version Barbell Version 1.2

@about Contains a list of the various url defined web-requests

        *Root and Basic Pages:
            -empty url pattern <results in index page being displayed>
            -about screen

        *Group and User Features:
            -create group screen
            -general settings screen
            -group screen <group_id integer included as a 'dynamic' parameter>
            -group settings screen <also takes in group_id>

        *Profile and Authentication:
            -profile
                /self
                /other
            -register <creates new CustomUser>

        *Stats and Leaderboards:
            -Input Rep Stats 
            -Table <For viewing the stats in tabular format>
            -leaderboard
                /global
                /group

        *Password Reset Flow:
            -account/password-reset <This view initiates the password reset process>
            -account/password-reset/done <This is the view the user is redirected to after submitting the previous form>
            -account/password-reset-confirm <This view is accessed from the link sent in the email , uidb64 and token are used to ID the user & their request>
            -acount/password-reset-complete <This is final stage of the reset flow>

        *Custom and Overridden URLS
            -accounts/login <Exists to override the default login URL used by 'django-allauth', redirecting the user to a custom template while maintaining the allauth logic>
            -signin <custom login view replaces the default Django HTML template, but inherits the logic found in views.py -> serves as a custom entry point for the users to sign in to>
            
        *Ajax Calls
            -get_stats <executes the view function get_stats which collects and filters the current user's data populating the StatData class object. The function returns a json, but it is converted to a python list first>     
"""

from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import CustomLoginView, CustomLogoutView
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_screen, name='about'),
    path('creategroup/', views.creategroup_screen, name='create_group'),
    path('general_settings/', views.generalsettings_screen, name='general_settings'),
    path('group_screen/<int:group_id>/', views.group_screen, name='group_screen'),
    path('group_settings/<int:group_id>/', views.group_settings_screen, name='group_settings'),
    path('home/', views.home_screen, name='home'),
    path('input_stats/', views.input_stats_screen, name='input_stats'),
    path('privacy_screen/', views.privacy_screen, name='privacy'),
    path('profile/<int:profile_id>/', views.profile_screen, name='profile'),
    path('profile/settings/', views.profilesettings_screen, name='profilesettings'),
    path('register/', views.register_screen, name='register'),
    path('signin/', views.CustomLoginView.as_view(), name='signin'),
    path('leaderboard/global/', views.global_leaderboard, name='global_leaderboard'),
    path('leaderboard/group/<int:group_id>/', views.group_leaderboard, name='group_leaderboard'),
    path('account/password-reset/', PasswordResetView.as_view(from_email='barbellauth@socialbarbell.com', template_name="account/password_reset.html"), name='password_reset'),
    path('account/password-reset/done/', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('account/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('account/password-reset-complete/', PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name='password_reset_complete'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'), # Overriding allauth's login view
    path('get_stats/', views.get_stats, name = 'ajax_get_stats'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]




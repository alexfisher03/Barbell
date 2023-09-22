from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from .views import CustomLoginView

# this is Django built in email authentication 
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, 
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_screen, name='about'),
    path('creategroup/', views.creategroup_screen, name='create_group'),
    path('forgot_password/', views.forgotpassword_screen, name='forgot_password'),
    path('general_settings/', views.generalsettings_screen, name='general_settings'),
    path('group_screen/<int:group_id>/', views.group_screen, name='group_screen'),
    path('group_settings/<int:group_id>/', views.group_settings_screen, name='group_settings'),
    path('home/', views.home_screen, name='home'),
    path('input_rep_stats/', views.input_rep_stats_screen, name='input_rep_stats'),
    path('privacy_screen/', views.privacy_screen, name='privacy'),
    path('profile/self/', views.profile_self_screen, name='profile_self'),
    path('profile/other/', views.profile_other_screen, name='profile_other'),
    path('profile/settings/', views.profilesettings_screen, name='profilesettings'),
    path('register/', views.register_screen, name='register'),
    path('signin/', views.CustomLoginView.as_view(), name='signin'),
    path('table/', views.stat_screen, name='stat'),
    path('leaderboard/global/', views.global_leaderboard, name='global_leaderboard'),
    path('leaderboard/group/', views.group_leaderboard, name='group_leaderboard'),
    path('account/password-reset/', PasswordResetView.as_view(from_email='no-reply@yourdomain.com', template_name="account/password_reset.html"), name='password_reset'),
    path('account/password-reset/done/', PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name='password_reset_done'),
    path('account/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name='password_reset_confirm'),
    path('account/password-reset-complete/', PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name='password_reset_complete'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'), # Overriding allauth's login view
]

#for placeholder while in development
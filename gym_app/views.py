from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import TableData

def index(request):
    return render(request, 'index.html')

def about_screen(request):
    return render(request, 'about/about_screen.html')


def creategroup_screen(request):
    return render(request, 'creategroup/creategroup_screen.html')


def forgotpassword_screen(request):
    return render(request, 'forgot_password/forgotpassword_screen.html')


def generalsettings_screen(request):
    return render(request, 'general_settings/generalsettings_screen.html')


def group_screen(request):
    return render(request, 'group/group_screen.html')

@login_required
def group_settings_screen(request):
    return render(request, 'group_settings/group_settings_screen.html')


def home_screen(request):
    return render(request, 'home/home_screen.html')


def input_rep_stats_screen(request):
    return render(request, 'input_rep_stats/input_rep_stats_screen.html')


def privacy_screen(request):
    return render(request, 'privacy/privacy_screen.html')


def profile_other_screen(request):
    return render(request, 'profile/other/profile_other_screen.html')


def profile_self_screen(request):
    return render(request, 'profile/self/profile_self_screen.html')


def profilesettings_screen(request):
    return render(request, 'profile/settings/profilesettings_screen.html')


def register_screen(request):
    return render(request, 'register/register_screen.html')

def signin_screen(request):
    return render(request, 'signin/signin_screen.html')


def stat_screen(request):
    return render(request, 'table/stat_screen.html')

def global_leaderboard(request):
    return render(request, 'leaderboard/global/global_leaderboard_screen.html')

def group_leaderboard(request):
    return render(request, 'leaderboard/group/group_leaderboard_screen.html')


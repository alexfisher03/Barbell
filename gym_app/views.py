from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import TableData

def index(request):
    return render(request, 'index.html')

@login_required
def about_screen(request):
    return render(request, 'about/about_screen.html')

@login_required
def creategroup_screen(request):
    return render(request, 'creategroup/creategroup_screen.html')

@login_required
def forgotpassword_screen(request):
    return render(request, 'forgot_password/forgotpassword_screen.html')

@login_required
def generalsettings_screen(request):
    return render(request, 'general_settings/generalsettings_screen.html')

@login_required
def group_screen(request):
    return render(request, 'group/group_screen.html')

@login_required
def group_settings_screen(request):
    return render(request, 'group_settings/group_settings_screen.html')

@login_required
def home_screen(request):
    return render(request, 'home/home_screen.html')

@login_required
def init_screen(request):
    return render(request, 'init/init_screen.html')

@login_required
def input_rep_stats_screen(request):
    return render(request, 'input_rep_stats/input_rep_stats_screen.html')

@login_required
def privacy_screen(request):
    return render(request, 'privacy/privacy_screen.html')

@login_required
def profile_other_screen(request):
    return render(request, 'profile/other/profile_other_screen.html')

@login_required
def profile_self_screen(request):
    return render(request, 'profile/self/profile_self_screen.html')

@login_required
def profilesettings_screen(request):
    return render(request, 'profile/settings/profilesettings_screen.html')

@login_required
def register_screen(request):
    return render(request, 'register/register_screen.html')

@login_required
def signin_screen(request):
    return render(request, 'signing/signin_screen.html')

@login_required
def stat_screen(request):
    return render(request, 'table/stat_screen.html')

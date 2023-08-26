from .models import CustomUser, TableData, ImageMetadata
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm

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
    if not request.user.is_authenticated:
        return redirect('signin_screen')
    user = request.user
    custom_user = CustomUser.objects.get(username=user.username)
    table_data = TableData.objects.filter(user=request.user)
    images = ImageMetadata.objects.filter(user=request.user)
    return render(request, 'profile/self/profile_self_screen.html', {
    'table_data': table_data, 
    'images': images, 
    'custom_user': custom_user
})


def profilesettings_screen(request):
    return render(request, 'profile/settings/profilesettings_screen.html')

def register_screen(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'register/register_screen.html', {'form': form, 'success': True})
    
    else:
        form = RegistrationForm()  # Ensure this line is properly indented and is outside of the POST block

    return render(request, 'register/register_screen.html', {'form': form})

def signin_screen(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile_self')
        else:
            try:
                user = CustomUser.objects.get(phone=username)
                if user.check_password(password):
                    login(request, user)
                    return redirect('profile_self')
            except CustomUser.DoesNotExist:
                pass
            messages.error(request, 'Invalid username or password.')
    return render(request, 'signin/signin_screen.html')


def stat_screen(request):
    return render(request, 'table/stat_screen.html')

def global_leaderboard(request):
    return render(request, 'leaderboard/global/global_leaderboard_screen.html')

def group_leaderboard(request):
    return render(request, 'leaderboard/group/group_leaderboard_screen.html')


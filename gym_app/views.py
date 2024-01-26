"""
@author Alexander Fisher & Jonathan Salem
@version Barbell Version 1

@about Contains the backend python functions and class objects that 
       handle and interact with various web requests and render responses
"""

from allauth.account.views import LoginView
from allauth.account.views import PasswordResetView as AllauthPasswordResetView
from .models import CustomUser, TableData, ImageMetadata, Group, StatData
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, BACKEND_SESSION_KEY
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ProfileSettings, CreateGroup, GroupSettings, StatForm
from django.http import JsonResponse

"""
Takes in the Django 'AllauthPasswordResetView' class object as a parameter, but 
explicitly sets the template to use. Allows the url to take in this object
and inherit the logic with a custom view template.
"""
class CustomPasswordResetView(AllauthPasswordResetView):
    template_name = 'account/password_reset.html'

"""
Customizes the login functionality that comes with Django's default by extending
the parameter 'LoginView', firstly by using the get method to render the custom
signin screen, and then secondly using the post method to access user authentication
to verify username and password entries. 
"""
class CustomLoginView(LoginView):

    def get(self, request, *args, **kwargs):
        return render(request, 'signin/signin_screen.html')

    def post(self, request, *args, **kwargs):
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

# static screen function
def index(request):
    return render(request, 'index.html')

# static screen function
def about_screen(request):
    return render(request, 'about/about_screen.html')

"""
Function using the CreateGroup form-class-object, which takes in
the 'forms.Modelform' parameter, enabling it to write to the Group
model-class-object. With this in mind, the form is creating the new
Group model for the user, and populating the values using the user's inputs.

Additionally, worth noting is that Django creates a random int, 'group_id' during
the url redirection process which can represent each group, and can 
handily be called using the Group data model object itself 
"""
@login_required
def creategroup_screen(request):
    if request.method == 'POST':
        form = CreateGroup(request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.created_by = request.user
            new_group.privacy = form.cleaned_data['privacy']
            new_group.save()
            request.user.current_group = new_group
            request.user.save()
            return redirect('group_screen', group_id=new_group.id)
        else:
            print("Form Errors:", form.errors)
    else:
        form = CreateGroup()
    return render(request, 'creategroup/creategroup_screen.html', {'form': form})

# static screen function
def generalsettings_screen(request):
    return render(request, 'general_settings/generalsettings_screen.html')

"""
Function gets the user's group object, contains placehold member logic to
ensure the user is in the group and to populate the HTML UI.
"""
@login_required
def group_screen(request, group_id):
    user = request.user
    group = Group.objects.get(id=group_id)

    members = group.group_members.all() # < - CHECK FIX
    
    is_user_in_group = user in members # this is checking to see if the logged in user is in the group
    other_members = [member for member in members if member != user]

    context = {
        'group': group,
        'self_user': user if is_user_in_group else None,
        'other_members': other_members,
        'current_group': group,
    }
    return render(request, 'group/group_screen.html', context)

"""
In developement
"""
def group_leaderboard(request, group_id):
    user = request.user
    group = Group.objects.get(id=group_id)
    members = group.group_members.all()

    # in developement
    
    return render(request, 'leaderboard/group/group_leaderboard_screen.html')

@login_required
def group_settings_screen(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    print("debug group fetched:", group)

    if request.user != group.created_by:
        return redirect('group_screen') # eventually create a message screen saying user cannot access 

    members = group.group_members.all()
    print("members fetched:", members)
    if len(members) < 1:
        return redirect('group_screen', group_id=group_id) # if group was deleted add message screen

    if request.method == 'POST':
        form = GroupSettings(request.POST, instance=group)
        if form.is_valid():
            updated_group = form.save(commit=False)
            updated_group.privacy = form.cleaned_data['privacy']
            updated_group.save()
            return redirect('group_screen', group_id=group_id)
        else:
            print(form.errors)
    if not group:
        return redirect('group_screen')
    else:
        form = GroupSettings(instance=group, group=group)

    context = {
        'form': form,
        'group': group,
        'members': members
    }

    return render(request, 'group_settings/group_settings_screen.html', context)

def home_screen(request):
    return render(request, 'home/home_screen.html')

@login_required
def input_rep_stats_screen(request):
    if request.method == 'POST':
        form = StatForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    return render(request, 'input_rep_stats/input_rep_stats_screen.html')

def get_stats(request):
    dataS = list(StatData.objects.filter(user=request.user).values())
    return JsonResponse(dataS, safe=False)

def stat_screen(request):
    return render(request, 'table/stats_screen.html')

def privacy_screen(request):
    return render(request, 'privacy/privacy_screen.html')

def profile_other_screen(request):
    return render(request, 'profile/other/profile_other_screen.html')

@login_required
def profile_self_screen(request):
    print(request.user.is_authenticated)
    custom_user = request.user
    table_data = TableData.objects.filter(user=request.user)
    images = ImageMetadata.objects.filter(user=request.user)
    current_group = request.user.current_group
    context = {
        'table_data': table_data, 
        'images': images, 
        'custom_user': custom_user,
        'current_group': current_group
    }
    my_groups = Group.objects.filter(created_by=request.user)
    return render(request, 'profile/self/profile_self_screen.html', context)


@login_required
def profilesettings_screen(request):
    print('Function Loaded')
    print(f"Current User: {request.user}")
    print(f"Request Method: {request.method}")
    user = request.user
    if request.method == 'POST':
       form = ProfileSettings(request.POST, request.FILES, instance=user)
       if form.is_valid():
           user = form.save(commit=False)
           if form.cleaned_data['profile_picture']:
               user.profile_picture = form.cleaned_data['profile_picture']
           if form.cleaned_data['bio']:
               user.bio = form.cleaned_data['bio']
           user.save()
           return redirect('profile_self')
       else:
           print(form.errors)
           for error in form.errors:
               messages.error(request, f"{error}: {form.errors[error]}")
    else:
        print('I did not post')
        form = ProfileSettings(instance=user)
    return render(request, 'profile/settings/profilesettings_screen.html', {'form': form})


def register_screen(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            backend = 'django.contrib.auth.backends.ModelBackend'
            user.backend = backend
            login(request, user)
            return render(request, 'register/register_screen.html', {'form': form, 'success': True})
        else:
            print("form is invalid", form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'register/register_screen.html', {'form': form})

def global_leaderboard(request):
    return render(request, 'leaderboard/global/global_leaderboard_screen.html')




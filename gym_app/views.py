from allauth.account.views import LoginView
from allauth.account.views import PasswordResetView as AllauthPasswordResetView
from .models import CustomUser, TableData, ImageMetadata, Group
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, BACKEND_SESSION_KEY
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ProfileSettings, CreateGroup, GroupSettings
from django.http import JsonResponse


class CustomPasswordResetView(AllauthPasswordResetView): # This inherits the allauth view but explictly sets the template
    template_name = 'account/password_reset.html'

def index(request):
    return render(request, 'index.html')

def about_screen(request):
    return render(request, 'about/about_screen.html')

@login_required
def creategroup_screen(request):
    if request.method == 'POST':
        form = CreateGroup(request.POST)
        if form.is_valid():
            print("Cleaned Data:", form.cleaned_data)
            new_group = form.save(commit=False)
            new_group.created_by = request.user
            new_group.privacy = form.cleaned_data['privacy']
            new_group.save()
            request.user.current_group = new_group
            request.user.save()
            print("New Group ID: ", new_group.id)
            print("New Group Privacy: ", new_group.privacy)
            return redirect('group_screen', group_id=new_group.id)
        else:
            print("Form Errors:", form.errors)
    else:
        print('Not post')
        form = CreateGroup()
    return render(request, 'creategroup/creategroup_screen.html', {'form': form})


#retired logic because letting Django handle it with allauth
#def forgotpassword_screen(request):

    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        allowed_special_characters = set("!@$#%&*")
        disallowed_characters = set("()^=+")
        
        try:
            user = CustomUser.objects.get(username=username) 
        except CustomUser.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return render(request, 'forgot_password/forgotpassword_screen.html')

        if any(char in disallowed_characters for char in new_password):
            messages.error(request, "Invalid special characters used. Please refrain from using (, ), ^, =, or +.")
            return render(request, 'forgot_password/forgotpassword_screen.html')
                        
        if not any(char in allowed_special_characters for char in new_password):
            messages.error(request, "Password must contain at least one of the following special characters: !, @, , $, %, &, *.")
            return render(request, 'forgot_password/forgotpassword_screen.html')

        if len(new_password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
            return render(request, 'forgot_password/forgotpassword_screen.html')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'forgot_password/forgotpassword_screen.html')

        user.set_password(new_password)
        user.save()
        messages.success(request, "Password has been reset.")
        context['success'] = True
        return redirect('signin')   #Redirect to the login page
    return render(request, 'forgot_password/forgotpassword_screen.html')

    

def generalsettings_screen(request):
    return render(request, 'general_settings/generalsettings_screen.html')

@login_required
def group_screen(request, group_id):
    user = request.user
    group = Group.objects.get(id=group_id)
    members = group.group_members.all()
    
    is_user_in_group = user in members #this is checking to see if the logged in user is in the group
    other_members = [member for member in members if member != user]

    context = {
        'group': group,
        'self_user': user if is_user_in_group else None,
        'other_members': other_members,
        'current_group': group,
    }
    return render(request, 'group/group_screen.html', context)

def group_leaderboard(request, group_id):
    group = Group.objects.get(id=group_id)
    #setup later for group leaderboard
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

def input_rep_stats_screen(request):
    return render(request, 'input_rep_stats/input_rep_stats_screen.html')

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
            login(request, user)
            backend = 'django.contrib.auth.backends.ModelBackend'
            user.backend = backend
            return render(request, 'register/register_screen.html', {'form': form, 'success': True})
        else:
            print("form is invalid", form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'register/register_screen.html', {'form': form})



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

def global_leaderboard(request):
    return render(request, 'leaderboard/global/global_leaderboard_screen.html')

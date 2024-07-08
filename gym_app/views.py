"""
@author Alexander Fisher
@version Barbell Version 1.2

@about Contains the backend python functions and class objects that 
       handle and interact with various web requests and render responses
"""

from typing import Any
from allauth.account.views import LoginView
from allauth.account.views import PasswordResetView as AllauthPasswordResetView
from .models import CustomUser, TableData, Group, StatData, ImageMetadata
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, BACKEND_SESSION_KEY
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ProfileSettings, CreateGroup, GroupSettings, StatForm
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.middleware.csrf import get_token

def csrf_test(request):
    csrf_token = get_token(request)
    response = JsonResponse({"Fucking fucker": "CSRF cookie is an fuck",
                                "litle tokern": csrf_token})
    response.set_cookie('csrftoken', csrf_token)
    return response

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
            get_token(request)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile', profile_id=user.id)
            else:
                try:
                    user = CustomUser.objects.get(phone=username)
                    if user.check_password(password):
                        login(request, user)
                        return redirect('profile', profile_id=user.id)
                except CustomUser.DoesNotExist:
                    pass
                messages.error(request, 'Invalid username or password.')
            return render(request, 'signin/signin_screen.html')
    
"""
Customizes the logout html template but with built in Django logout view logic. Additionally, 
in select HTML templates we want to hide certain elements usually inherited by the index.html 
(parent file). In order to do this for the footer in the logout screen, we set the 'show_footer'
variable '= False' within the context dict, all inside the built in Django LogoutView
"""
class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_footer'] = False
        return context

# static render function
def index(request):
    context = {
        'is_index_page': True,
        'is_admin': request.user.is_staff or request.user.is_superuser,
        }
    return render(request, 'index.html', context)

# static render function
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
    get_token(request)
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

# static render function
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

    context = {
        'group': group,
        'members': members,
    }
    
    
    return render(request, 'leaderboard/group/group_leaderboard_screen.html', context)


"""
Function gets the defined group_id's Group object and firstly does 
a check on whether the user created the group or not (accessing the created_by attribute)
& checks to see if the amount of members exist (i.e the group exists)

The function then checks if the user POST contains data populated in the form on the UI,
and then creates an instance of the GroupSettings form-class-object. The form is firstly 
set to a variable but not saved to the database yet, the privacy data from the settings 
form is collected before, then it finally saves. 
"""
@login_required
def group_settings_screen(request, group_id):
    get_token(request)
    group = get_object_or_404(Group, id=group_id)

    if request.user != group.created_by:
        messages.error(request, "You don't have permission to access this page.")
        return redirect('group_screen')

    form = GroupSettings(request.POST, instance=group, group=group)

    if request.method == 'POST':
        if form.is_valid():
            updated_group = form.save(commit=False)
            updated_group.name = form.cleaned_data.get('name')
            updated_group.groupbio = form.cleaned_data.get('groupbio')
            updated_group.privacy = form.cleaned_data.get('privacy')
            
            members_to_remove = form.cleaned_data.get('members_to_remove')
            for member in members_to_remove:
                if group.created_by in members_to_remove:
                    group.delete()
                    messages.success(request, "The group has been deleted.")
                    return redirect('profile', profile_id=request.user.id)
            
                group.group_members.remove(member)
            
            updated_group.save()
            form.save_m2m()

            if members_to_remove == group.created_by:
                updated_group.delete()
                messages.success(request, "The group has been deleted.")
                return redirect('profile', profile_id=request.user.id)

            messages.success(request, "Group settings updated successfully.")
            return redirect('group_screen', group_id=group_id)

    context = {
        'form': form,
        'group': group,
        'members': group.group_members.all()
    }
    return render(request, 'group_settings/group_settings_screen.html', context)


# static render function
def home_screen(request):
    return render(request, 'home/home_screen.html')

"""
This function contains a form that collects user inputs to populate the 
attributes of the StatData model class-object. The POST request is saved
using the StatForm class-object, which is handled during the URL routing process 
at the '/get_stats' address; which utilizes the get_stats view function.  
"""
@login_required
def input_stats_screen(request):
    if request.method == 'POST':
        form = StatForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    return render(request, 'input_stats/input_stats_screen.html')

def get_stats(request):
    dataS = list(StatData.objects.filter(user=request.user).values())
    return JsonResponse(dataS, safe=False)

# static render function
def privacy_screen(request):
    return render(request, 'privacy/privacy_screen.html')


"""
This function initializes variables representing the various data attributes of the CustomUser model,
along with featuring the TableData model attributes (this is where the workout splits are stored for now)
The variables declared in the context of this function are then used locally within the context dictionary
as key value pairs, where the keys are called in the HTML templates, thus allowing for the correct data to 
populate the different user profile screens.
"""
@login_required
def profile_screen(request, profile_id):
    # check if the profile id matches the logged in user
    if profile_id == request.user.id:
        profile = request.user
    # uses the dynamically created profile id value i.e. another user
    else:
        profile = get_object_or_404(CustomUser, id=profile_id)
    
    # fetching profile specific data from the model class object
    table_data = TableData.objects.filter(user=profile)
    images = ImageMetadata.objects.filter(user=profile)
    current_group = profile.current_group

    if profile == request.user:
        my_groups = Group.objects.filter(created_by=profile)
    else:
        my_groups = None

    context = {
        'profile': profile,
        'table_data': table_data, 
        'images': images, 
        'custom_user': request.user,
        'current_group': current_group,
        'my_groups': my_groups,
    }
    
    return render(request, 'profile/profile_screen.html', context)

"""
Handles the user's ProfileSettings form class-object POST request. Uses cleaned_data method
on the two form user input fields and populates the object attributes with those values. This 
upon saving by .save() method will update the user's profile picture and bio data entries. 
""" 
@login_required
def profilesettings_screen(request):
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
           return redirect('profile', profile_id=user.id)
       else:
           for error in form.errors:
               messages.error(request, f"{error}: {form.errors[error]}")
    else:
        form = ProfileSettings(instance=user)
    return render(request, 'profile/settings/profilesettings_screen.html', {'form': form})

"""
This function handles the RegistrationForm user inputs. Again, the user's inputs 
populate the various attributes within the Form Object, and if the form is valid it saves.

However a key feature here is that the backend variable assigned to the value of 
'django.contrib.auth.backends.ModelBackend' exists because this method is a built in
Django authentication method. In other words, it will automatically verify the given username
and password by comparing the given username to the hashed password stored in the database. 

An additional note - the default ModelBackend method looks for the default Django user model.
In the case of this application, found in settings.py within the project directory, an override
declaration "AUTH_USER_MODEL = 'gym_app.CustomUser'" defines the fact that this application uses a 
custom user model , "CustomUser" (found in models.py) instead. 
"""
def register_screen(request):
    get_token(request)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
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
 
# static render function - needs fix
def global_leaderboard(request):
    return render(request, 'leaderboard/global/global_leaderboard_screen.html')

"""
Logic for the 404 error page
"""
def custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', {}, status=404)

"""
Logic for the 500 error page
"""
def custom_internal_server_error_view(request, *args, **kwargs):
    return render(request, 'errors/500.html', {}, status=500)
"""
@author Alexander Fisher
@version Barbell Version 1.2

@about Defines 'form' class objects within the html templates. Instances of the 
       objects contain the information used in the POST request within view logic.
       This data is then integrated into the SQL data structure.       
"""
from django import forms
from .models import CustomUser, Group, Workout
from django.core.exceptions import ValidationError
from django.forms import ModelForm

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'gender', 'profile_picture']  

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        allowed_special_characters = set("!@#$%&*")
        disallowed_characters = set("()^=+")

        if any(char in disallowed_characters for char in password1):
            raise forms.ValidationError("Invalid special characters used. Please refrain from using (, ), =, or +.")
                
        if not any(char in allowed_special_characters for char in password1):
            raise forms.ValidationError("Password must contain at least one of the following special characters: !, @, #, $, %, &, *.")
        
        if password1 and len(password1) < 6:
            raise forms.ValidationError("Passwords must be at least 6 characters long.")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class ProfileSettings(forms.ModelForm):
    profile_picture = forms.ImageField(label='Change Profile Picture:', widget=forms.FileInput, required=False)
    bio = forms.CharField(label='Change Profile Bio:', widget=forms.TextInput, required=False)

    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture']

    def clean_profile_picture(self):
        image = self.cleaned_data.get('profile_picture')        
        if image:
            if image.size > 2*1024*1024:
                raise forms.ValidationError("Image file size may not exceed 2MB.")
            content_type = image.content_type
            if content_type not in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Only JPEG or PNG images allowed.")
        return image

    def clean(self):
        cleaned_data = super().clean()
        bio = cleaned_data.get('bio')
        profile_picture = cleaned_data.get('profile_picture')

        # Check that at least one field is filled
        if not bio and profile_picture is None:
            raise forms.ValidationError("You must select at least one setting to change.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
class CreateGroup(forms.ModelForm):
    # group name
    name = forms.CharField(label='Group Name', widget=forms.TextInput, required=True)
    groupbio = forms.CharField(label='Bio', widget=forms.TextInput, required=True)
    privacy = forms.ChoiceField(
        choices=[
            ('PUB', 'Public'),
            ('PRV', 'Private')
        ],
        widget=forms.RadioSelect
    )
    class Meta:
        model = Group
        fields = ['name', 'groupbio', 'privacy']

class GroupSettings(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'groupbio']

    members_to_remove = forms.ModelMultipleChoiceField(
        queryset=CustomUser.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    
    privacy = forms.ChoiceField(
        choices=[
            ('PUB', 'Public'),
            ('PRV', 'Private')
        ],
        widget=forms.RadioSelect,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        group = kwargs.pop('group', None)
        super(GroupSettings, self).__init__(*args, **kwargs)
        if group:
            self.fields['members_to_remove'].queryset = group.group_members.all()
            self.fields['privacy'].initial = group.privacy

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']
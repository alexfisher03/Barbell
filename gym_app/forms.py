from django import forms
from .models import CustomUser, Group
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'gender', 'profile_picture']  

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
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
        if hasattr(image, 'content_type'):
            content_type = image.content_type
        elif hasattr(image, 'file') and hasattr(image.file, 'content_type'):
            content_type = image.file.content_type
        else:
            return None          
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
    groupname = forms.CharField(label='Group Name', widget=forms.TextInput, required=True)
    biogroup = forms.CharField(label='Bio', widget=forms.TextInput, required=True)
    gprivacy = forms.ChoiceField(
        choices=[
            ('PUB', 'Public'),
            ('PRV', 'Private')
        ],
        widget=forms.RadioSelect
    )
    class Meta:
        model = Group
        fields = ['groupname', 'biogroup', 'gprivacy']
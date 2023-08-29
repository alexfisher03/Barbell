from django import forms
from .models import CustomUser
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
        if not image:
            raise forms.ValidationError("This field is required. ")
        if hasattr(image, 'content_type'):
            content_type = image.content_type
        elif hasattr(image, 'file') and hasattr(image.file, 'content_type'):
            content_type = image.file.content_type
        else:
            raise forms.ValidationError("Could not determine the content type of the image.")
        if content_type not in ['image/jpeg', 'image/png']:
            raise forms.ValidationError("Only JPEG or PNG images allowed.")
        return image
    
    def clean(self):
        cleaned_data = super().clean()
        bio = cleaned_data.get('bio')
        profile_picture = cleaned_data.get('profile_picture')

        if not bio and not profile_picture:
            raise forms.ValidationError("You must select at least one setting to change.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    
#ignore
    # def clean_profile_picture(self):
        image = self.cleaned_data.get('profile_picture')
        if not image:
            raise forms.ValidationError("This field is required. ")
        content_type = getattr(image, 'content_type', None)
        if content_type is None and hasattr(image, 'file'):
            content_type = getattr(image.file, 'content_type', None)       
        if content_type not in ['image/jpeg', 'image/png']:
            raise forms.ValidationError("Only JPEG or PNG images allowed.")
        return image
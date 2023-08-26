from django import forms
from .models import CustomUser

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
    profile_picture = forms.ImageField(label='Change Profile Picture:', widget=forms.FileInput)
    bio = forms.CharField(label='Change Profile Bio:', widget=forms.TextInput)

    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture']
    
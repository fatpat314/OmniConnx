from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateFormNone(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional']


class ProfileUpdateFormStudent(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional', 'test']


class ProfileUpdateFormProfessional(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional', 'test']

class ProfileUpdateFormBoth(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'student', 'professional', 'test']
